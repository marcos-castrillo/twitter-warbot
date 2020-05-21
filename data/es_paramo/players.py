#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Name, username, gender, place, weapon_list
raw_player_list = [
    [u'Sr.Willy', u'guillerfc', 0, u'Villagallegos'],
    [u'Amaia', u'AmaiaaLgn', 1, u'Laguna de Negrillos'],
    [u'María', u'mariaa_gcia', 1, u'Valencia de Don Juan'],
    [u'', u'Porulinda', 1, u'Cabreros del Río'],
    [u'Nuria', u'Nuriiti_07', 1, u'Cembranos'],
    [u'Iván', u'Ivanmm_12', 0, u'Riego de la Vega'],
    [u'Álex', u'alex15_gch', 0, u'Villamañán'],
    [u'Cascon', u'cascoon7', 0, u'Valencia de Don Juan'],
    [u'Ainhoa', u'ainhoaLgn', 1, u'Laguna de Negrillos'],
    [u'Natalia', u'Natsuarez20', 1, u'Villaestrigo del Páramo'],
    [u'Conchi', u'ConchiCalderon', 1, u'Bercianos del Páramo'],
    [u'Veronica', u'VeronicaCastri', 1, u'Bercianos del Páramo'],
    [u'Sheila', u'Sheiilanerea00', 1, u'Zambroncinos'],
    [u'Luis', u'Luisseijas_98', 0, u'Villar del Yermo'],
    [u'Pedro', u'PedroMateo4', 0, u'Villamañán'],
    [u'María', u'mmayvieira', 1, u'Celadilla del Páramo'],
    [u'', u'mcv_19', 1, u'Villamañán'],
    [u'Raúl', u'raauulrgz', 0, u'Cabreros del Río'],
    [u'Alfonso', u'ElBuenChiki', 0, u'Bercianos del Páramo'],
    [u'Paula', u'pbntzh', 1, u'Bercianos del Páramo'],
    [u'Sara', u'saraaalonso__', 1, u'Cembranos'],
    [u'Laura', u'LaurAldao', 1, u'Villibañe'],
    [u'', u'SpaceGambol', 1, u'Villibañe'],
    [u'Maite', u'MaiteCasado', 1, u'Bercianos del Páramo'],
    [u'Bea', u'BeaCaL', 1, u'Bercianos del Páramo'],
    [u'Carmen', u'CarmenTejedor1', 1, u'Villamañán'],
    [u'Sara', u'saara_rguezz', 1, u'Villamañán'],
    [u'David', u'daviddeleon33', 0, u'Cembranos'],
    [u'Hugo', u'hugoblannco_', 0, u'Cembranos'],
    [u'Iker', u'iikeer3', 0, u'Cembranos'],
    [u'Bea', u'beeitaa21', 1, u'Cembranos'],
    [u'', u'yisii_', 0, u'Cembranos'],
    [u'Centeno', u'CentenoDavid5', 0, u'Cebrones del Río'],
    [u'Andrea', u'andreadrewww', 1, u'Cembranos'],
    [u'Cristina', u'crisssmaart', 1, u'Cebrones del Río'],
    [u'Abel', u'santamariastar1', 0, u'Santa María del Páramo'],
    [u'Víctor', u'Victoriano_15', 0, u'Villamorico'],
    [u'Rosa', u'larosaliaaa', 1, u'Bercianos del Páramo'],
    [u'Óscar', u'oski99_lgn', 0, u'Laguna de Negrillos'],
    [u'Javi', u'JaviDeLonge182', 0, u'Bercianos del Páramo'],
    [u'Pablo', u'pablincounter', 0, u'Cembranos'],
    [u'Diana', u'didiixdd', 1, u'Santa María del Páramo'],
    [u'Laura', u'lauucch', 1, u'Bercianos del Páramo'],
    [u'Cloti', u'Claudia08teran', 1, u'Bercianos del Páramo'],
    [u'Jony', u'jony_JRM', 0, u'Bercianos del Páramo'],
    [u'Ivo', u'ivopd_01', 0, u'Bercianos del Páramo'],
    [u'Carla', u'__carlag', 1, u'Laguna de Negrillos'],
    [u'Lorena', u'lore_macu16', 1, u'Cebrones del Río'],
    [u'Sokram', u'Sokram', 0, u'Bercianos del Páramo'],
    [u'Sergio', u'SergioRenton', 0, u'Tabuyuelo de Jamuz'],
    [u'Noe', u'k3rfuffle_', 1, u'Roperuelos del Páramo'],
    [u'Lagandi', u'Lagandi', 0, u'Laguna de Negrillos'],
    [u'MiguelOne', u'amoaprispras', 0, u'Santa María del Páramo'],
    [u'Ángela', u'Angelaapa', 1, u'Santa María del Páramo'],
    [u'Iván', u'ivxnyrc', 0, u'Bercianos del Páramo'],
    [u'Sara', u'saranatalperez', 1, u'Bercianos del Páramo'],
    [u'Álex', u'Alex_Stinson7', 0, u'Bercianos del Páramo'],
    [u'Robson', u'NBA_Fuckboy', 0, u'Santa María del Páramo'],
    [u'Eric', u'Eric_Almeda', 0, u'Bercianos del Páramo'],
    [u'García', u'J_Garcia_25', 0, u'Cabreros del Río'],
    [u'Clara', u'clarabntzz', 1, u'Bercianos del Páramo'],
    [u'Raquel', u'RaqueeLgn', 1, u'Laguna de Negrillos'],
    [u'Laura', u'lauriitalgn01', 1, u'Zambroncinos'],
    [u'Welin', u'WelintonSergist', 0, u'Villamorico'],
    [u'', u'nosoyuxue_', 1, u'Cabreros del Río'],
    [u'Aitana', u'AitanaFresno', 1, u'Palacios de Fontecha'],
    [u'Eva', u'laguneva', 1, u'Laguna de Negrillos'],
    [u'Rik', u'Rik3619', 0, u'Toral de los Guzmanes'],
    [u'Miguel', u'Miguii_10', 0, u'Villamorico'],
    [u'Abel', u'Dr_venenoo', 0, u'Zotes del Páramo'],
    [u'Yess', u'yessdguez_', 1, u'Santa María del Páramo'],
    [u'Lorena', u'Lorenapa1999', 1, u'Villamañán'],
    [u'Sonia', u'imanidi0tt', 1, u'Roperuelos del Páramo'],
    [u'Amaya', u'AmayaaMtnz', 1, u'Laguna de Negrillos'],
    [u'Paula', u'pauulapelaezz', 1, u'Laguna de Negrillos'],
    [u'Lucía', u'luciarierapres', 1, u'León'],
    [u'Samuel', u'Samuelgarrido88', 0, u'Valencia de Don Juan'],
    [u'Lía', u'liacxstillo', 1, u'León'],
    [u'Pablo', u'Pablo_mtz98', 0, u'Villadangos del Páramo'],
    [u'Sergio', u'cazusergi', 0, u'Villagallegos'],
    [u'Iván', u'ivanmrdm', 0, u'Valencia de Don Juan'],
    [u'Pabluco', u'Pabluco_97', 0, u'Valencia de Don Juan'],
    [u'Samu', u'samucente8', 0, u'Cebrones del Río'],
    [u'Amanda', u'AmandaBeneitez', 1, u'Palacios de Fontecha'],
    [u'Kela', u'Keelaa17', 1, u'Villagallegos'],
    [u'Pablo', u'pablodpp', 0, u'Carrizo de la Ribera'],
    [u'David', u'Dav1darme', 0, u'Armellada'],
    [u'Nayara', u'NayaraMilla1', 1, u'La Milla del Río'],
    [u'', u'_She_W0lf_', 1, u'Villibañe'],
    [u'Ale', u'alegoncar_', 1, u'Valencia de Don Juan'],
    [u'Ángela', u'14Angeelaaa', 1, u'Fojedo'],
    [u'Sara', u'saraarllen', 1, u'Fojedo'],
    [u'María', u'Mariialvvarez', 1, u'Fojedo'],
    [u'Nerey', u'ivrognee', 1, u'Bercianos del Páramo'],
    [u'Josele', u'jose_martrod', 0, u'Villar del Yermo'],
    [u'Víctor', u'Victor_SM98', 0, u'San Martín del Camino'],
    [u'Elena', u'elenaa__125', 1, u'San Martín del Camino'],
    [u'Iván', u'Ivan_96leon', 0, u'San Martín del Camino'],
    [u'Mirian', u'Mirian_grisu', 1, u'Grisuela del Páramo'],
    [u'Miriam', u'miriamx02', 1, u'Villar de Mazarife'],
    [u'Zurdy', u'zurdy6', 0, u'Valderrey'],
    [u'Javi', u'javieralonso495', 0, u'Valderrey'],
    [u'Carlos', u'carlossutil_', 0, u'Grisuela del Páramo'],
    [u'Leticia', u'LeticiaGrisuela', 1, u'Grisuela del Páramo'],
    [u'María', u'Mariia0609', 1, u'Santa María del Páramo'],
    [u'Kini', u'danibercy', 0, u'Villamorico'],
    [u'Álvaro', u'alvaropglzz_', 0, u'Armellada'],
    [u'Nick', u'Epsil0n_5', 0, u'Armellada'],
    [u'Alicia', u'_aliciarguez', 1, u'Bercianos del Páramo'],
    [u'Eva', u'EvaLauraAE', 1, u'Villaestrigo del Páramo'],
    [u'Lucía', u'Luciamorang', 1, u'Villaestrigo del Páramo'],
    [u'Yani', u'yani_myea', 1, u'Cembranos'],
    [u'Melissa', u'MelissaShelbyy', 1, u'Grisuela del Páramo'],
    [u'Raquel', u'raquelbntzz', 1, u'Bercianos del Páramo'],
    [u'Aarón', u'aron_maiden', 0, u'Villamorico'],
    [u'Jake', u'JakeDerbyshire', 0, u'Celadilla del Páramo'],
    [u'Lucilda', u'luciferceive', 1, u'Celadilla del Páramo'],
    [u'Mata', u'dani1229mata', 0, u'Santa María del Páramo'],
    [u'Pérez', u'javierperezJP', 0, u'Villamorico'],
    [u'Inés', u'InesSutil', 0, u'Grisuela del Páramo'],
    [u'Adrio', u'Adrio_aac', 0, u'Villamorico'],
    [u'Quique', u'quiquemeando', 0, u'Villamorico'],
    [u'Lucía', u'luciaa_rio', 1, u'Valdevimbre'],
    [u'Cristina', u'cristina_rey95', 1, u'Villamañán'],
    [u'Rouus', u'JdBm23n16', 1, u'Santa María del Páramo'],
    [u'Andrea', u'andreacolado06', 1, u'Fojedo'],
    [u'David', u'davidalegree7', 0, u'Villagallegos'],
    [u'Darío', u'dariooalvareez', 0, u'Carrizo de la Ribera'],
    [u'Marta', u'martacimadevill', 1, u'Villadangos del Páramo'],
    [u'Óscar', u'oscarinrisi', 0, u'Villadangos del Páramo'],
    [u'Oliver', u'0liversparrow', 0, u'Villadangos del Páramo'],
    [u'Katia', u'KatiaGon10', 1, u'Fojedo'],
    [u'Miguel', u'MiguiDePan', 0, u'Bercianos del Páramo'],
    [u'Andrea', u'andreagperez99', 1, u'Villadangos del Páramo'],
    [u'Diego', u'Apache_BaMbAm', 1, u'Ardoncino'],

    #No RT o follow
    #[u'Andrea', u'andree_228', 1, u'Laguna de Negrillos'],
    #[u'Hugo', u'huugocalleejo_', 0, u'Villagallegos'],
    #[u'Víctor', u'vixtor2', 0, u'Valdevimbre'],
    #[u'Darío', u'darioxx5', 0, u'Valdevimbre'],

    #lugar incorrecto
    #[u'César', u'cgcJC', 0, u'Valjunco'],

    #Cuenta privada

]
