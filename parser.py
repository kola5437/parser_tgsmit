# -*- coding: utf8 -*-
import requests
from bs4 import BeautifulSoup
from xml.dom import minidom
import datetime
import time
from progress.bar import IncrementalBar

FILE = 'tgsmit'
today = datetime.datetime.today()
time1 = today.strftime("%Y-%m-%d %H:%M:%S")
start = time.monotonic()

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}

num_for = 0
num = 0

HOST = 'https://www.tgsmit.ru'

URL = ''

b = []



links = ['https://www.tgsmit.ru/catalog/stroymaterialy/steny_i_peregorodki/gipsokarton/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/stroymaterialy/steny_i_peregorodki/napravlyayushchie_i_profili/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/stroymaterialy/steny_i_peregorodki/fanera/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/stroymaterialy/steny_i_peregorodki/dsp/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/stroymaterialy/steny_i_peregorodki/dvp/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/stroymaterialy/steny_i_peregorodki/kirpich/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/stroymaterialy/steny_i_peregorodki/gazobeton/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/stroymaterialy/steny_i_peregorodki/komplektuyushchie_k_profilyam/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/stroymaterialy/steny_i_peregorodki/paneli_osb_3/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/stroymaterialy/sukhie_stroitelnye_smesi/shtukaturki/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/stroymaterialy/sukhie_stroitelnye_smesi/shpatlevki/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/stroymaterialy/sukhie_stroitelnye_smesi/tsement/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/stroymaterialy/sukhie_stroitelnye_smesi/rovniteli/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/stroymaterialy/sukhie_stroitelnye_smesi/kley_dlya_plitki_i_montazha/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/stroymaterialy/sukhie_stroitelnye_smesi/zatirki_dlya_plitochnykh_shvov/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/stroymaterialy/sukhie_stroitelnye_smesi/sypuchie_materialy/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/stroymaterialy/pilomaterialy/derevyannye_izdeliya/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/stroymaterialy/pilomaterialy/polovaya_reyka/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/stroymaterialy/pilomaterialy/vagonka/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/stroymaterialy/pilomaterialy/nalichniki/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/stroymaterialy/pogonazh/bruski/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/stroymaterialy/pogonazh/plintusa/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/stroymaterialy/pogonazh/raskladki/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/stroymaterialy/pogonazh/ugolki/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/stroymaterialy/pogonazh/shtapiki/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/stroymaterialy/izolyatsiya/teploizolyatsiya/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/stroymaterialy/izolyatsiya/gidro_paro_vetroizolyatsiya/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/stroymaterialy/izolyatsiya/penoplast/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/stroymaterialy/izolyatsiya/podlozhka/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/stroymaterialy/izolyatsiya/plenka_polietilenovaya/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/stroymaterialy/izolyatsiya/porolon/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/stroymaterialy/izolyatsiya/paklya/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/stroymaterialy/metalloprokat/elektrody/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/stroymaterialy/metalloprokat/setka/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/stroymaterialy/metalloprokat/armatura/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/stroymaterialy/metalloprokat/pechnoe_lite/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/stroymaterialy/vintovoy_fundament/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/krovlya_i_fasad/metallocherepitsa_i_komplektuyushchie/metallocherepitsa/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/krovlya_i_fasad/metallocherepitsa_i_komplektuyushchie/komplektuyushchie_k_metallocherepitse/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/krovlya_i_fasad/ondulin/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/krovlya_i_fasad/myagkaya_krovlya/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/krovlya_i_fasad/shifer/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/krovlya_i_fasad/sayding/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/krovlya_i_fasad/profnastil/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/krovlya_i_fasad/ploskiy_list/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/krovlya_i_fasad/sistema_vodostoka/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/krovlya_i_fasad/ventiliruemyy_fasad/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/krovlya_i_fasad/gibkaya_cherepitsa/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/krovlya_i_fasad/sistema_ograzhdeniy/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/lako_krasochnye_materialy/kraski/izvest/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/lako_krasochnye_materialy/kraski/kolery/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/lako_krasochnye_materialy/kraski/gotovye_shpatlevki/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/lako_krasochnye_materialy/kraski/dekorativnaya_shtukaturka/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/lako_krasochnye_materialy/emali_1/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/lako_krasochnye_materialy/gruntovki_1/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/lako_krasochnye_materialy/derevozashchita/lak_1/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/lako_krasochnye_materialy/derevozashchita/olifa_1/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/lako_krasochnye_materialy/derevozashchita/antiseptiki/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/lako_krasochnye_materialy/malyarnye_instrumenty/nabory_malyarnye/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/lako_krasochnye_materialy/malyarnye_instrumenty/kisti/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/lako_krasochnye_materialy/malyarnye_instrumenty/valiki/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/lako_krasochnye_materialy/malyarnye_instrumenty/sterzhni_teleskopicheskie/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/lako_krasochnye_materialy/aerozolnye_kraski_sprey/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/napolnye_pokrytiya/laminat/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/napolnye_pokrytiya/linoleum/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/napolnye_pokrytiya/plitka_pvkh/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/napolnye_pokrytiya/komplektuyushchie_dlya_pola/plintusa_1/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/napolnye_pokrytiya/komplektuyushchie_dlya_pola/porogi/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/napolnye_pokrytiya/komplektuyushchie_dlya_pola/kley_dlya_napolnykh_pokrytiy/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/napolnye_pokrytiya/komplektuyushchie_dlya_pola/podlozhka_1/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/napolnye_pokrytiya/kovry_1/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/napolnye_pokrytiya/kovrolin_2/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/napolnye_pokrytiya/kovriki_pridvernye/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/oboi/flizelinovye_oboi/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/oboi/vinilovye_oboi/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/oboi/oboi_pod_pokrasku/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/oboi/plenka_samokleyashchayasya/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/oboi/zhidkie_oboi/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/oboi/steklooboi/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/oboi/steklooboi/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/oboi/bumazhnye_oboi/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/oboi/bumazhnye_oboi/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/oboi/instrument_dlya_pokleyki_oboev/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/dveri/dveri_mezhkomnatnye/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/dveri/dveri_vkhodnye_metallicheskie/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/dveri/dveri_razdvizhnye/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/dveri/dvernye_arki/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/dveri/dvernye_korobki_nalichniki_i_dobory/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/plitka/keramicheskaya_plitka/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/plitka/keramicheskiy_granit/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/plitka/mozaika_1/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/plitka/raskhodnye_materialy/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/osveshchenie/lyustry/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/osveshchenie/nastenno_potolochnye_svetilniki/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/osveshchenie/torshery/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/osveshchenie/svetilniki/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/osveshchenie/svetodiodnye_dekorativnye_lampy/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/osveshchenie/osveshchenie_tekhnicheskoe/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/osveshchenie/ulichnoe_osveshchenie/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/santekhnika_mebel_i_tovary_dlya_vannoy/vodonagrevateli/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/santekhnika_mebel_i_tovary_dlya_vannoy/vanny/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/santekhnika_mebel_i_tovary_dlya_vannoy/dushevye_kabiny_i_ograzhdeniya/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/santekhnika_mebel_i_tovary_dlya_vannoy/poddony_dushevye/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/santekhnika_mebel_i_tovary_dlya_vannoy/mebel_dlya_vannoy/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/santekhnika_mebel_i_tovary_dlya_vannoy/polotentsesushiteli/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/santekhnika_mebel_i_tovary_dlya_vannoy/moyki/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/santekhnika_mebel_i_tovary_dlya_vannoy/sanfayans/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/santekhnika_mebel_i_tovary_dlya_vannoy/smesiteli_i_dushevoe_oborudovanie/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/santekhnika_mebel_i_tovary_dlya_vannoy/tovary_dlya_vannoy_komnaty/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/santekhnika_mebel_i_tovary_dlya_vannoy/santekhnika_dlya_invalidov_meditsinskikh_uchrezhdeniy/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/elektroinstrumenty/akkumulyatory/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/elektroinstrumenty/betonosmesiteli_1/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/elektroinstrumenty/generatory_puskozaryadnye_ustroystva/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/elektroinstrumenty/dreli_perforatory_otboynye_molotki/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/elektroinstrumenty/izmeritelnaya_tekhnika_1/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/elektroinstrumenty/komressory_kraskopulty_pylesosy/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/elektroinstrumenty/lobziki_shtroborezy_nozhnitsy_plitkorezy/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/elektroinstrumenty/pily_diskovye_lentochnye/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/elektroinstrumenty/rubanki_reymusy_freyzery_stanki/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/elektroinstrumenty/svarochnye_apparaty_1/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/elektroinstrumenty/stanki_zatochnye_sverlilnye/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/elektroinstrumenty/feny_stroitelnye_kleevye_pistolety_1/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/elektroinstrumenty/uglovye_shlifmashiny_1/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/elektroinstrumenty/tsepnye_pily_i_komplektuyushchie/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/elektroinstrumenty/shlifmashiny_1/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/elektroinstrumenty/shurupoverty_gaykoverty/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/elektrotovary/konditsionery_i_ventilyatory/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/elektrotovary/kabel/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/elektrotovary/rozetki_i_vyklyuchateli/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/elektrotovary/lampy/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/elektrotovary/lenty_svetodiodnye/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/elektrotovary/fonari/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/elektrotovary/schetchiki/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/elektrotovary/udliniteli/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/elektrotovary/stabilizatory/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/elektrotovary/avtomatika/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/elektrotovary/aksessuary_dlya_elektromontazha/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/elektrotovary/obogrevateli_kaminy_i_teplyy_pol/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/ruchnye_instrumenty_1/ruchnye_instrumenty/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/ruchnye_instrumenty_1/izmeritelnye_instrumenty/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/ruchnye_instrumenty_1/verevki_i_shpagaty/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/ruchnye_instrumenty_1/lestnitsy_i_stremyanki/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/ruchnye_instrumenty_1/sredstva_zashchity_truda/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/ruchnye_instrumenty_1/yashchiki_dlya_instrumentov/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/ruchnye_instrumenty_1/osnastka_dlya_elektroinstrumentov/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/ruchnye_instrumenty_1/meshki_metla_veniki/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/ventilyatsiya/ventilyatory/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/ventilyatsiya/reshetki_i_kanaly/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/ventilyatsiya/lyuki_santekhnicheskie/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/krepezhnye_izdeliya/samorezy/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/krepezhnye_izdeliya/skoby/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/krepezhnye_izdeliya/ankery/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/krepezhnye_izdeliya/gvozdi/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/krepezhnye_izdeliya/dyubeli/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/krepezhnye_izdeliya/zaklepki/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/krepezhnye_izdeliya/metricheskiy_krepezh/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/krepezhnye_izdeliya/perforirovannyy_krepezh/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/krepezhnye_izdeliya/takelazh/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/teplo_vodosnabzhenie/radiatory/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/teplo_vodosnabzhenie/nasosnoe_oborudovanie/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/teplo_vodosnabzhenie/vodosnabzhenie/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/teplo_vodosnabzhenie/vodootvedenie/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/teplo_vodosnabzhenie/kotelnoe_oborudovanie/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/zamochno_skobyanye_izdeliya/zamki_interernye/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/zamochno_skobyanye_izdeliya/zamki_stroitelnye_skobyanye_izdeliya/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/lenty_setki_skotchi/lenty_1/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/lenty_setki_skotchi/serpyanki/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/lenty_setki_skotchi/setki/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/lenty_setki_skotchi/skotchi_1/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/lenty_setki_skotchi/uplotniteli_1/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/lenty_setki_skotchi/obivka_dlya_dverey/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/pena_germetiki_kley/pena/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/pena_germetiki_kley/germetiki_1/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/pena_germetiki_kley/kley_1/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/interer/paneli_stenovye/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/interer/potolki/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/interer/komplektuyushchie_dlya_otdelki/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/interer/postelnoe_bele_1/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/interer/postelnye_prinadlezhnosti_1/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/interer/karniz/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/interer/pledy_i_pokryvala/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/interer/lepnoy_dekor_1/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/interer/polki_interernye_1/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/interer/zhalyuzi_1/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/interer/shtory_rulonnye_2/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/interer/shtory_tekstilnye_1/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/sadovo_ogorodnyy_inventar/sadovyy_instrument_2/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/sadovo_ogorodnyy_inventar/ukryvnoy_material/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/sadovo_ogorodnyy_inventar/sotovyy_polikarbonat/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/sadovo_ogorodnyy_inventar/teplitsy_parniki/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/sadovo_ogorodnyy_inventar/plenka_polietilenovaya_1/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/sadovo_ogorodnyy_inventar/shlangi_rasseivateli_dlya_vody/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/sadovo_ogorodnyy_inventar/parniki/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/sadovo_ogorodnyy_inventar/pochvogrunt/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/khozyaystvennye_tovary_1/otsinkovannye_izdeliya/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/khozyaystvennye_tovary_1/ukhod_za_domom/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/khozyaystvennye_tovary_1/bytovaya_khimiya_i_gigiena/?PAGEN_{0}=2&SIZEN_2=12','https://www.tgsmit.ru/catalog/khozyaystvennye_tovary_1/izdeliya_iz_plastmassy/?PAGEN_{0}=2&SIZEN_2=12',
'https://www.tgsmit.ru/catalog/okna_i_komplektuyushchie/?PAGEN_{0}=2&SIZEN_2=12']

a = ['152','154','153','146','150','151','147','148','155',
     '139','141','144','145','143','142','140','160','157',
     '158','156','161','166','165','164','163','178','180',
     '179','162','177','176','181','182','183','185','184',
     '132','198','199','197','195','196','193','192','191',
     '186','188','187','194','211','210','209','208','206',
     '205','214','213','203','216','217','215','219','201',
     '222','226','225','227','229','230','228','223','221',
     '220','231','240','238','239','236','237','234','235',
     '233','232','241','246','245','244','243','247','249',
     '248','242','256','257','251','255','254','253','252',
     '263','267','266','265','264','262','261','260','258',
     '259','250','281','283','282','279','277','280','278',
     '275','276','272','274','273','268','271','270','269',
     '286','292','295','293','291','290','289','288','284',
     '285','287','294','303','297','301','300','298','302',
     '299','296','304','305','306','312','315','314','313',
     '310','311','308','309','307','319','320','316','317','318','323','321','323',
     '328','326','327','325','329','332','331','330','341',
     '340','339','335','334','336','342','337','338','333',
     '343','344','348','350','353','345','349','347','346',
     '351','355','354','356','352','173']
lin = []
mylist = [len(links)]


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r



def get_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='rw_category-main__item')
    for item in items:
        links = item.find('a', class_='rw_product-card__wrapper').get('href')
        link = HOST + links
        parser_links(link) 


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    cat = soup.find_all('span',class_='rw_characteristics__list-cell')
    img_link = soup.find_all('div',class_='rw_preview__image')
    price_l = soup.find_all('span',class_='rw_card-price__current-value js-item-price')
    for i in price_l:
        price = i
    for i in img_link:
        img = i

    if len(cat) == 12:
        lin.append({
                'id':b,
                'price':price.get_text(),
                'title': soup.find('h1',class_='rw_product-info__heading').get_text(),
                'xar':soup.find('div',class_='rw_info-accordeon__panel-text').get_text(),
                'categories':categories,
                'p1': cat[0].get_text() + ' ' + cat[6].get_text(),
                'p2': cat[1].get_text() + ' ' + cat[7].get_text(),
                'p3': cat[2].get_text() + ' ' + cat[8].get_text(),
                'p4': cat[3].get_text() + ' ' + cat[9].get_text(),
                'p5': cat[4].get_text() + ' ' + cat[10].get_text(),
                'p6': cat[5].get_text() + ' ' + cat[11].get_text(),
                'image':HOST + img.find('img',class_='js-image-preview rw_preview__image-placeholder').get('src')
            })
    elif len(cat) == 8:
        lin.append({
                'id':b,
                'price':price.get_text(),
                'title': soup.find('h1',class_='rw_product-info__heading').get_text(),
                'xar':soup.find('div',class_='rw_info-accordeon__panel-text').get_text(),
                'categories':categories,
                'p1': cat[0].get_text() + ' ' + cat[4].get_text(),
                'p2': cat[1].get_text() + ' ' + cat[5].get_text(),
                'p3': cat[2].get_text() + ' ' + cat[6].get_text(),
                'p4': cat[3].get_text() + ' ' + cat[7].get_text(),
                'p5':'',
                'p6': '',
                'image':HOST + img.find('img',class_='js-image-preview rw_preview__image-placeholder').get('src')
            })
    elif len(cat) == 10:
        lin.append({
                'id':b,
                'price':price.get_text(),
                'title': soup.find('h1',class_='rw_product-info__heading').get_text(),
                'xar':soup.find('div',class_='rw_info-accordeon__panel-text').get_text(),
                'categories':categories,
                'p1': cat[0].get_text() + ' ' + cat[5].get_text(),
                'p2': cat[1].get_text() + ' ' + cat[6].get_text(),
                'p3': cat[2].get_text() + ' ' + cat[7].get_text(),
                'p4': cat[3].get_text() + ' ' + cat[8].get_text(),
                'p5': cat[4].get_text() + ' ' + cat[9].get_text(),
                'p6': '',
                'image':HOST + img.find('img',class_='js-image-preview rw_preview__image-placeholder').get('src')
            })
    elif len(cat) == 6:
        lin.append({
                'id':b,
                'price':price.get_text(),
                'title': soup.find('h1',class_='rw_product-info__heading').get_text(),
                'xar':soup.find('div',class_='rw_info-accordeon__panel-text').get_text(),
                'categories':categories,
                'p1': cat[0].get_text() + ' ' + cat[3].get_text(),
                'p2': cat[1].get_text() + ' ' + cat[4].get_text(),
                'p3': cat[2].get_text() + ' ' + cat[5].get_text(),
                'p4': '',
                'p5': '',
                'p6': '',
                'image':HOST + img.find('img',class_='js-image-preview rw_preview__image-placeholder').get('src')
            })
    elif len(cat) == 4:
        lin.append({
                'id':b,
                'price':price.get_text(),
                'title': soup.find('h1',class_='rw_product-info__heading').get_text(),
                'xar':soup.find('div',class_='rw_info-accordeon__panel-text').get_text(),
                'categories':categories,
                'p1': cat[0].get_text() + ' ' + cat[2].get_text(),
                'p2': cat[1].get_text() + ' ' + cat[3].get_text(),
                'p3': '',
                'p4': '',
                'p5': '',
                'p6': '',
                'image':HOST + img.find('img',class_='js-image-preview rw_preview__image-placeholder').get('src')
            })
    elif len(cat) == 2:
        lin.append({
                'id':b,
                'price':price.get_text(),
                'title': soup.find('h1',class_='rw_product-info__heading').get_text(),
                'xar':soup.find('div',class_='rw_info-accordeon__panel-text').get_text(),
                'categories':categories,
                'p1': cat[0].get_text() + ' ' + cat[1].get_text(),
                'p2': '',
                'p3': '',
                'p4': '',
                'p5': '',
                'p6':' ',
                'image':HOST + img.find('img',class_='js-image-preview rw_preview__image-placeholder').get('src')
            })   
    elif len(cat) == 0:
        lin.append({
                'id':b,
                'price':price.get_text(),
                'title': soup.find('h1',class_='rw_product-info__heading').get_text(),
                'xar':soup.find('div',class_='rw_info-accordeon__panel-text').get_text(),
                'categories':categories,
                'p1': '',
                'p2': '',
                'p3': '',
                'p4': '',
                'p5': '',
                'p6':' ',
                'image':HOST + img.find('img',class_='js-image-preview rw_preview__image-placeholder').get('src')
            })
def parser_links(links):
    html = get_html(links)
    if html.status_code == 200:
        cars = get_content(html.text)
    else:
        pass


def get_page(html,URL):
    global categories
    soup = BeautifulSoup(html, 'html.parser')
    categorie = soup.find('h2',class_='rw_category-main__title intersection-title').get_text()
    try:
        if ' – cтраница 2' in categorie:
            categories = categorie.replace(' – cтраница 2', '') 
        num_link = soup.find_all('a', class_='rw_category-main__pagination-link')
        if len(num_link) == 1:
            parser(int(num_link[0].get_text()))
        else:
            del num_link[-1]
            num11 = num_link[-1].get_text()
            num1 = int(num11)
            parser(num1)
    except Exception as e:
        return 0

def parser_first():
    global url1
    global b
    global num_for
    bar = IncrementalBar('Прогресс ', max = len(links))

    for url in links:
        bar.next()

        url1 = url
        b = a[num_for]

        num_for = num_for + 1
        URL = url.format('1')
        html = get_html(URL)
        if html.status_code == 200:
            cars = get_page(html.text,URL)
        else:
            pass


def parser(num1):
    
    global num
    num = 1
    for i in range(num1):
        URL = url1.format(num)
        num += 1
        html = get_html(URL)
        if html.status_code == 200:
            cars = get_links(html.text)
        else:
            time.sleep(2)
            return 1





def save():
    root = minidom.Document()

    xml_root = root.createElement('listings')
    root.appendChild(xml_root)
    for item in lin:
        id = item['id']
        price = item['price']
        title = item['title']
        content = item['xar']
        categories = item['categories']
        p1 = item['p1']
        p2 = item['p2']
        p3 = item['p3']
        p4 = item['p4']
        p5 = item['p5']
        p6 = item['p6']
        image = item['image']

        categoriesChild = root.createElement('listing')
        xml_root.appendChild(categoriesChild)

        categoryChild = root.createElement('title')
        categoryChild.setAttribute('lang', f'ru-RU')
        categoryText = root.createCDATASection(title)
        categoryChild.appendChild(categoryText)

        contentChild = root.createElement('content')
        contentChild.setAttribute('lang', f'ru-RU')
        content = root.createCDATASection(content)
        contentChild.appendChild(content)

        catChild = root.createElement('category')
        catChild.setAttribute('lang', f'ru-RU')
        catText = root.createTextNode(categories)
        catChild.appendChild(catText)

        categoryidChild = root.createElement('categoryid')
        categoryidText = root.createTextNode(id)
        categoryidChild.appendChild(categoryidText)

        contactemailChild = root.createElement('contactemail')
        contactemailText = root.createTextNode('avtor1@mail.ru')
        contactemailChild.appendChild(contactemailText)

        contactnameChild = root.createElement('contactname')
        contactnameText = root.createTextNode('Avtor1')
        contactnameChild.appendChild(contactnameText)

        priceChild = root.createElement('price')
        priceText = root.createTextNode(price)
        priceChild.appendChild(priceText)

        currencyChild = root.createElement('currency')
        currencyText = root.createTextNode('RUB')
        currencyChild.appendChild(currencyText)

        city_areaChild = root.createElement('city_area')
        city_areaText = root.createTextNode('670000')
        city_areaChild.appendChild(city_areaText)
        
        cityChild = root.createElement('city')
        cityText = root.createTextNode('Улан-Удэ')
        cityChild.appendChild(cityText)

        regionChild = root.createElement('region')
        regionText = root.createTextNode('Республика Бурятия')
        regionChild.appendChild(regionText)

        countryIdChild = root.createElement('countryId')
        countryIdText = root.createTextNode('RUS')
        countryIdChild.appendChild(countryIdText)

        countryChild = root.createElement('country')
        countryText = root.createTextNode('Россия')
        countryChild.appendChild(countryText)

        tgChild = root.createElement('custom')
        tgChild.setAttribute('name', f'tip')
        tgText = root.createTextNode('ТГ СМИТ')
        tgChild.appendChild(tgText)

        artChild = root.createElement('custom')
        artChild.setAttribute('name',f'p1')
        artText = root.createTextNode(p1)
        artChild.appendChild(artText)

        waterChild = root.createElement('custom')
        waterChild.setAttribute('name',f'p2')
        waterText = root.createTextNode(p2)
        waterChild.appendChild(waterText)

        markChild = root.createElement('custom')
        markChild.setAttribute('name',f'p3')
        markText = root.createTextNode(p3)
        markChild.appendChild(markText)

        materialChild = root.createElement('custom')
        materialChild.setAttribute('name',f'p4')
        materialText = root.createTextNode(p4)
        materialChild.appendChild(materialText)

        application_typeChild = root.createElement('custom')
        application_typeChild.setAttribute('name',f'p5')
        application_typeText = root.createTextNode(p5)
        application_typeChild.appendChild(application_typeText)

        scope_of_applicationChild = root.createElement('custom')
        scope_of_applicationChild.setAttribute('name',f'p6')
        scope_of_applicationText = root.createTextNode(p6)
        scope_of_applicationChild.appendChild(scope_of_applicationText)

        imageChild = root.createElement('image')
        imageText = root.createTextNode(image)
        imageChild.appendChild(imageText)

        dataChild = root.createElement('datetime')
        dataText = root.createTextNode(time1)
        dataChild.appendChild(dataText)


        categoriesChild.appendChild(categoryChild)
        categoriesChild.appendChild(contentChild)
        categoriesChild.appendChild(catChild)
        categoriesChild.appendChild(categoryidChild)
        categoriesChild.appendChild(contactemailChild)
        categoriesChild.appendChild(contactnameChild)
        categoriesChild.appendChild(priceChild)
        categoriesChild.appendChild(currencyChild)
        categoriesChild.appendChild(city_areaChild)
        categoriesChild.appendChild(cityChild)
        categoriesChild.appendChild(regionChild)
        categoriesChild.appendChild(countryIdChild)
        categoriesChild.appendChild(countryChild)
        categoriesChild.appendChild(tgChild)
        categoriesChild.appendChild(artChild)
        categoriesChild.appendChild(waterChild)
        categoriesChild.appendChild(markChild)
        categoriesChild.appendChild(materialChild)
        categoriesChild.appendChild(application_typeChild)
        categoriesChild.appendChild(scope_of_applicationChild)
        categoriesChild.appendChild(imageChild)
        categoriesChild.appendChild(dataChild)


    xml_root.appendChild(categoriesChild)
    xml_str = root.toprettyxml(indent="\t")
    save_path_file = (str(FILE) + '.yml')
    
    with open(save_path_file, "w",encoding='utf-8') as f:
        f.write(xml_str)
for i in range(100):
    parser_first()
    save()
    end = time.monotonic()
    print('Создан файл ' + FILE + '.yml')
    print('Время  : {:>9.2f}'.format(end - start))
    a = input('')
