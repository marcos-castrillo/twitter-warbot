import boto3
import os
import twitter
from secrets import *

dir_name = 'simulations'

line_filename_suffix = '_line.txt'
image_filename_suffix = '_image.txt'
simulation_filename = 'simulation.txt'

img_file_extension = '.png'
img_bis_suffix = '_bis'
map_filename_suffix = '_map'
ranking_filename_suffix = '_ranking'

session = boto3.Session(aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
s3 = session.resource('s3')
s3_client = session.client('s3')
bucket_name = 'paramobot'
my_bucket = s3.Bucket(bucket_name)


def get_api():
    return twitter.Api(consumer_key=api_key,
                       consumer_secret=api_secret,
                       access_token_key=access_token,
                       access_token_secret=access_token_secret)


def tweet(message, image_path_list):
    image_list = []

    if image_path_list is not None:
        for i, path in enumerate(image_path_list):
            if path is not None and os.path.exists(path):
                image_list.append(path)

    api = get_api()
    tweet_obj = api.PostUpdate(status=message, media=image_list)
    return tweet_obj.id_str


def tweet_line_from_file(file_path, line_number, image_path_list=[]):
    i = 0
    for line in file_path.get()['Body'].iter_lines():
        if i == int(line_number):
            line = line.decode('UTF-8')
            linebreaks = line.count('//n')
            if linebreaks > 0:
                line = line.replace('//n', '\n')
            print(line)
            return tweet(line, image_path_list)
        i = i + 1


def get_file(filename):
    return s3.Object(bucket_name=bucket_name, key=dir_name + '/' + filename)


def get_file_path(filename):
    path = '/tmp/' + filename
    if file_exists(filename):
        s3_client.download_file(bucket_name, dir_name + '/' + filename, path)
        return path
    else:
        return None


def file_exists(filename):
    objs = list(my_bucket.objects.filter(Prefix=dir_name + "/" + filename))
    return len(objs) == 1 and objs[0].key == dir_name + "/" + filename


def rename_file(old_filename, new_filename):
    my_bucket.copy({'Bucket': bucket_name, 'Key': dir_name + '/' + old_filename}, dir_name + '/' + new_filename)
    response = s3_client.delete_object(Bucket=bucket_name, Key=dir_name + '/' + old_filename)


def lambda_handler(event, context):
    # Get number of total lines and next line to tweet
    total_lines = 0
    next_line = None
    next_image = None
    simulation_file = get_file(simulation_filename)

    for line in simulation_file.get()['Body'].iter_lines():
        if next_line is None and file_exists(str(total_lines) + line_filename_suffix):
            next_line = total_lines + 1
        if next_image is None and file_exists(str(total_lines) + image_filename_suffix):
            next_image = total_lines + 1
        total_lines = total_lines + 1
        pass

    # Tweet line
    main_image_path = get_file_path(str(next_image) + img_file_extension)
    map_image_path = get_file_path(str(next_image) + map_filename_suffix + img_file_extension)
    ranking_image_path = get_file_path(str(next_image) + ranking_filename_suffix + img_file_extension)
    image_path_list = [main_image_path, map_image_path, ranking_image_path]
    tweet_line_from_file(simulation_file, next_line, image_path_list)
    # Rename next_line and next_image files
    rename_file(str(next_line - 1) + line_filename_suffix, str(next_line) + line_filename_suffix)
    rename_file(str(next_image - 1) + image_filename_suffix, str(next_image) + image_filename_suffix)
    # Check if there's a follow-up (bis) tweet
    main_image_path = get_file_path(str(next_image) + img_bis_suffix + img_file_extension)
    if main_image_path != None:
        # Tweet line
        next_line = next_line + 1
        image_path_list = [main_image_path]
        tweet_line_from_file(simulation_file, next_line, image_path_list)
        # Rename next_line file
        rename_file(str(next_line - 1) + line_filename_suffix, str(next_line) + line_filename_suffix)

    return {
        'statusCode': 200
    }
