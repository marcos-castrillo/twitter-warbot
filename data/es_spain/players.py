#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Name, username, gender, place, weapon_list
raw_player_list = [
    [u'Álvaro Ojeda', u'alvaroojeda80', 0, u'Cádiz'],
    [u'Ada Colau', u'AdaColau', 1, u'Barcelona'],
    [u'Adrilik', u'adrilik', 0, u'Barcelona'],
    [u'Aitana', u'Aitanax', 1, u'Barcelona'],
    [u'Alba Reche', u'_albxreche', 1, u'Alicante'],
    [u'Albert Rivera', u'Albert_Rivera', 0, u'Barcelona'],
    [u'Alberto Chicote', u'albertochicote', 0, u'Madrid'],
    [u'Alberto Garzón', u'agarzon', 0, u'Logroño'],
    [u'Alexby11', u'aLexBY11', 0, u'Madrid'],
    [u'Alexelcapo', u'EvilAFM', 0, u'Palma de Mallorca'],
    [u'Alfredo Duro', u'alfredoduro1', 0, u'Madrid'],
    [u'Amaia Romero', u'amaiaromero', 1, u'Pamplona'],
    [u'Ana Milán', u'_ANAMILAN_', 1, u'Alicante'],
    [u'Ana Rosa Quintana', u'anarosaq', 1, u'Madrid'],
    [u'Ander Cortés', u'G2Ander', 0, u'Bilbao'],
    [u'Andreu Buenafuente', u'Buenafuente', 0, u'Tarragona'],
    [u'Andrés Iniesta', u'andresiniesta8', 0, u'Albacete'],
    [u'Antonio Castelo', u'SrCastelo', 0, u'Alicante'],
    [u'Antonio Lobato', u'alobatof1', 0, u'Oviedo'],
    [u'Arkano', u'SmoothArkano', 0, u'Alicante'],
    [u'Aron Piper', u'EsAronPiper', 0, u''],
    [u'Arturo Pérez Reverte', u'perezreverte', 0, u'Murcia'],
    [u'Arturo Valls', u'ArturoValls', 0, u'Valencia'],
    [u'AuronPlay', u'auronplay', 0, u'Barcelona'],
    [u'Ayax y Prok', u'ayaxyprok', 0, u'Granada'],
    [u'Bad gyal', u'', 1, u'Barcelona'],
    [u'Bejo', u'Bejoflow', 0, u'Santa Cruz de Tenerife'],
    [u'Belén Esteban', u'BelenEstebanM', 1, u'Madrid'],
    [u'Berto Romero', u'Berto_Romero', 0, u'Barcelona'],
    [u'C. Tangana', u'c_tangana', 0, u'Madrid'],
    [u'Carles Puigdemont', u'KRLS', 0, u'Girona'],
    [u'Carles Puyol', u'Carles5puyol', 0, u'Lleida'],
    [u'Cristóbal Soria', u'cristobalsoria', 0, u'Sevilla'],
    [u'Dani Martín', u'_danielmartin_', 0, u'Madrid'],
    [u'Chincheto', u'chincheto77', 0, u'Madrid'],
    [u'Christian Gálvez', u'ChristianG_7', 0, u'Madrid'],
    [u'Cristina Pedroche', u'CristiPedroche', 1, u'Madrid'],
    [u'Dalas Review', u'DalasReview', 0, u'Santa Cruz de Tenerife'],
    [u'Dani Martínez', u'danimartinezweb', 0, u'León'],
    [u'Dani Mateo', u'DaniMateoAgain', 0, u'Barcelona'],
    [u'Dani Rovira', u'DANIROVIRA', 0, u'Málaga'],
    [u'Dario Eme Hache', u'darioemehache', 0, u'Madrid'],
    [u'David Bisbal', u'davidbisbal', 0, u'Almería'],
    [u'David Broncano', u'davidbroncano', 0, u'A Coruña'],
    [u'David Bustamante', u'David_Busta', 0, u'Santander'],
    [u'DayoScript', u'DayoScript', 0, u'Madrid'],
    [u'DjMaRiiO', u'DjMaRiiO_90', 0, u'Madrid'],
    [u'Don Patricio', u'don_patricito', 0, u'Santa Cruz de Tenerife'],
    [u'El Rubius', u'Rubiu5', 0, u'Málaga'],
    [u'ElRichMC', u'ElRichMC', 0, u'A Coruña'],
    [u'Esperanza Aguirre', u'EsperanzAguirre', 1, u'Madrid'],
    [u'Esperanza Gracia', u'esperanzagracia', 1, u'Madrid'],
    [u'Eva Hache', u'eva_hache', 1, u'Segovia'],
    [u'Fargan', u'xFaRgAnx', 0, u'Toledo'],
    [u'Fernando Alonso', u'alo_oficial', 0, u'Oviedo'],
    [u'Fernando Costa', u'', 0, u'Palma de Mallorca'],
    [u'Fernando Simón', u'', 0, u'Zaragoza'],
    [u'Fernando Tejero', u'fertejerom', 0, u'Córdoba'],
    [u'Fortfast', u'SrFortfast', 0, u'Granada'],
    [u'Frank Cuesta', u'Frank_Cuesta', 0, u'León'],
    [u'Gabriel Rufián', u'gabrielrufian', 0, u'Barcelona'],
    [u'Gerard Piqué', u'3gerardpique', 0, u'Barcelona'],
    [u'Guti', u'GUTY14HAZ', 0, u'Madrid'],
    [u'Ibai Llanos', u'IbaiLlanos', 0, u'Bilbao'],
    [u'Ignatius Farray', u'IgnatiusFarray', 0, u'Santa Cruz de Tenerife'],
    [u'Iker Casillas', u'IkerCasillas', 0, u'Madrid'],
    [u'Iker Jiménez', u'navedelmisterio', 0, u'Vitoria'],
    [u'Inés Arrimadas', u'InesArrimadas', 1, u'Cádiz'],
    [u'InstaSamer', u'InstaSamer', 0, u'Málaga'],
    [u'Iñigo Errejón', u'ierrejon', 0, u'Madrid'],
    [u'Irene Montero', u'IreneMontero', 1, u'Madrid'],
    [u'Jaime Altozano', u'jaimealtozano', 0, u'Madrid'],
    [u'Felipez360', u'Felipez360', 0, u'Guadalajara'],
    [u'Hamza Zaidi', u'hamzazaidi97', 0, u''],
    [u'Jesús Vázquez', u'_JesusVazquez_', 0, u'A Coruña'],
    [u'Joaquín Reyes', u'enjutomojamuto', 0, u'Albacete'],
    [u'JoaquínPA', u'J0aquinPA', 0, u'Palma de Mallorca'],
    [u'Jordi Cruz', u'JordiCruzPerez', 0, u'Barcelona'],
    [u'Jordi ENP', u'jordiporn', 0, u'Ciudad Real'],
    [u'Jordi Wild', u'JordiWild', 0, u'Barcelona'],
    [u'Jorge Javier Vázquez', u'jjaviervazquez', 0, u'Barcelona'],
    [u'Jorge Ponce', u'jponcerivero', 0, u'Málaga'],
    [u'José Mota', u'JoseMotatv', 0, u'Ciudad Real'],
    [u'Juan Mata', u'juanmata8', 0, u'Burgos'],
    [u'Juan Ramón Rallo', u'juanrallo', 0, u'Castellón de la Plana'],
    [u'Kase O', u'KaseO_real', 0, u'Zaragoza'],
    [u'Kidd Keo', u'KiddKeo95Flames', 0, u'Alicante'],
    [u'KNekro', u'KNekro', 0, u'Madrid'],
    [u'LMDShow', u'LMDShow', 0, u'Málaga'],
    [u'Lolito Fdez', u'LOLiTOFDEZ', 0, u'Málaga'],
    [u'Loulogio', u'Loulogio_Pi', 0, u'Barcelona'],
    [u'Luis Cepeda', u'cepedaoficial', 0, u'Ourense'],
    [u'Luis Piedrahita', u'PiedrahitaLuis', 0, u'A Coruña'],
    [u'Luzu', u'LuzuVlogs', 0, u'Bilbao'],
    [u'Malú', u'_MaluOficial_', 1, u'Madrid'],
    [u'MangelRogel', u'mangelrogel', 0, u'Barcelona'],
    [u'Manuela Carmena', u'ManuelaCarmena', 1, u'Madrid'],
    [u'María Parrado', u'Mariaparradovoz', 1, u'Cádiz'],
    [u'Mariano Rajoy', u'marianorajoy', 0, u'A Coruña'],
    [u'Marina Yers', u'', 0, u''],
    [u'Martínez-Almeida', u'AlmeidaPP_', 0, u'Madrid'],
    [u'Melendi', u'MelendiOficial', 0, u'Oviedo'],
    [u'Miare', u'MIAREsproject', 1, u'Barcelona'],
    [u'Miguel Ángel Revilla', u'RevillaMiguelA', 0, u'Santander'],
    [u'Miki Nadal', u'NadalMiki', 0, u'Zaragoza'],
    [u'Miki Nuñez', u'mikinunez', 0, u'Barcelona'],
    [u'Miquel Montoro', u'', 0, u'Palma de Mallorca'],
    [u'Miriam Rodríguez', u'miriamrmusic_', 1, u'A Coruña'],
    [u'Míster Jägger', u'MisterJagger_', 0, u'Madrid'],
    [u'Nacho Vidal', u'NACHOVIDALPORN', 0, u'Barcelona'],
    [u'Natos y Waor', u'NatosyWaor', 0, u'Madrid'],
    [u'Natalia Lacunza', u'natalialacunza', 1, u'Pamplona'],
    [u'Orslok', u'orslok', 0, u'A Coruña'],
    [u'Pablo Alborán', u'pabloalboran', 0, u'Málaga'],
    [u'Pablo Casado', u'pablocasado_', 0, u'Palencia'],
    [u'Pablo Echenique', u'pnique', 0, u'Zaragoza'],
    [u'Pablo Iglesias', u'PabloIglesias', 0, u'Madrid'],
    [u'Pablo Motos', u'El_Hormiguero', 0, u'Valencia'],
    [u'Paco León', u'pacoleonbarrios', 0, u'Sevilla'],
    [u'Papi Gavi', u'papigavi', 0, u'Madrid'],
    [u'Patri la de Vox', u'paatri_guerrero', 1, u'Palma de Mallorca'],
    [u'Pau Gasol', u'paugasol', 0, u'Barcelona'],
    [u'Pedro Duque', u'astro_duque', 0, u'Madrid'],
    [u'Pedro Sánchez', u'sanchezcastejon', 0, u'Madrid'],
    [u'Pepe Viyuela', u'PepeViyuelactor', 0, u'Logroño'],
    [u'Perxitaa', u'Perxitaa', 0, u'Valencia'],
    [u'Rober Wido', u'wikiroberwido', 0, u'Bilbao'],
    [u'QuantumFracture', u'QuantumFracture', 0, u'Ciudad Real'],
    [u'Quequé', u'_Queque_', 0, u'Salamanca'],
    [u'Rafa Mora', u'RAFAMORATETE', 0, u'Valencia'],
    [u'Rafa Nadal', u'RafaelNadal', 0, u'Palma de Mallorca'],
    [u'Risto Mejide', u'ristomejide', 0, u'Barcelona'],
    [u'Rocío Monasterio', u'monasterioR', 1, u'Madrid'],
    [u'Roberto Leal', u'RobertoLealG', 0, u'Sevilla'],
    [u'Rosalía', u'rosalia', 1, u'Barcelona'],
    [u'Salvador Raya', u'SalvadorRaya', 0, u'Córdoba'],
    [u'Santiago Abascal', u'Santi_ABASCAL', 0, u'Bilbao'],
    [u'Santiago Segura', u'SSantiagosegura', 0, u'Madrid'],
    [u'Sr. Cheeto', u'Srcheeto', 0, u'Málaga'],
    [u'sTaXx', u'bysTaXx', 0, u'Castellón de la Plana'],
    [u'Telmo', u'Telmometro', 0, u'San Sebastián'],
    [u'Ter', u'tercosmicqueen', 1, u'Madrid'],
    [u'Tiparraco', u'TiparracoSA', 0, u'Zaragoza'],
    [u'TheGrefg', u'TheGrefg', 0, u'Murcia'],
    [u'Tomás Roncero', u'As_TomasRoncero', 0, u'Ciudad Real'],
    [u'Vegetta777', u'vegetta777', 0, u'Madrid'],
    [u'Wikiesqueletos', u'Wikiesqueletos', 0, u''],
    [u'Willyrex', u'WillyrexYT', 0, u'Madrid'],
    [u'Wismichu', u'Wismichu', 0, u'A Coruña'],
    [u'Yung Beef', u'secoweedcodein', 0, u'Granada'],

    [u'Eric Avilés', u'Eric_Almeda', 0, u'Oviedo'],
    [u'Scab', u'Scab__', 0, u'Lugo'],
    [u'Ángela Aparicio', u'Angelaapa', 1, u'León'],
    [u'Project Bercy', u'mariinajoseph', 1, u'León'],
    [u'Mafranpe', u'mafranpe', 0, u'Murcia'],
    [u'Luis Torres', u'luisalb42413076', 0, u'Toledo']
]
