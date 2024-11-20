from flask import Flask, render_template, request
from data import db_session
from data.movie import Movie
from data.theaters import Theater
import config as cfg
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
msg = MIMEMultipart()
to_email = "travellru@yandex.ru"
msg["From"] = cfg.LOGIN

@app.route("/question", methods=['POST', 'GET'])
def question():
    if request.method == 'GET':
        return render_template("question.html")
    elif request.method == 'POST':
        param = {}
        param['email'] = request.form['email']
        param['name'] = request.form['name']
        param['question'] = request.form['question']
        msg["Subject"] = f"Новый вопрос {param["name"]}"
        msg_body = f'Вопрос от: {param["email"]}\n' \
                   f'Автора вопроса зовут: {param["name"]}\n' \
                   f'Текст сообщения: {param["question"]}'
        msg.attach(MIMEText(msg_body, "plain"))
        server = smtplib.SMTP_SSL("smtp.yandex.com: 465")
        server.login(cfg.LOGIN, cfg.PASSWORD)
        server.sendmail(cfg.LOGIN, to_email, msg.as_string())
        return render_template('succes.html', title="Успешно")


# Главная страница
@app.route("/")
def home():
    return render_template("home.html")


#Регионы
@app.route("/region")
def region():
    return render_template("region.html")


# Далее страницы регионов
@app.route("/Altai_Territory")
def Altai_Territory():
    return render_template("Altai_Territory.html")


@app.route("/Altai_Territory_Nature")
def Altai_Territory_Nature():
    return render_template("Altai_Territory_Nature.html")


@app.route("/Amur_Region")
def Amur_Region():
    return render_template("Amur_Region.html")


@app.route("/Amur_Region_Nature")
def Amur_Region_Nature():
    return render_template("Amur_Region_Nature.html")


@app.route("/Astrakhan_Region")
def Astrakhan_Region():
    return render_template("Astrakhan_Region.html")


@app.route("/Astrakhan_Region_Nature")
def Astrakhan_Region_Nature():
    return render_template("Astrakhan_Region_Nature.html")


@app.route("/Arkhangelsk_Region")
def Arkhangelsk_Region():
    return render_template("Arkhangelsk_Region.html")


@app.route("/Arkhangelsk_Region_Nature")
def Arkhangelsk_Region_Nature():
    return render_template("Arkhangelsk_Region_Nature.html")


@app.route("/Belgorod_Region")
def Belgorod_Region():
    return render_template("Belgorod_Region.html")


@app.route("/Belgorod_Region_Nature")
def Belgorod_Region_Nature():
    return render_template("Belgorod_Region_Nature.html")


@app.route("/Bryansk_Region")
def Bryansk_Region():
    return render_template("Bryansk_Region.html")


@app.route("/Bryansk_Region_Nature")
def Bryansk_Region_Nature():
    return render_template("Bryansk_Region_Nature.html")


@app.route("/Vladimir_Region")
def Vladimir_Region():
    return render_template("Vladimir_Region.html")


@app.route("/Vladimir_Region_Nature")
def Vladimir_Region_Nature():
    return render_template("Vladimir_Region_Nature.html")


@app.route("/Volgograd_Region")
def Volgograd_Region():
    return render_template("Volgograd_region.html")


@app.route("/Volgograd_Region_Nature")
def Volgograd_Region_Nature():
    return render_template("Volgograd_Region_Nature.html")


@app.route("/Vologda_Region")
def Vologda_Region():
    return render_template("Vologda_region.html")


@app.route("/Vologda_Region_Nature")
def Vologda_Region_Nature():
    return render_template("Vologda_Region_Nature.html")


@app.route("/Voronezh_Region")
def Voronezh_Region():
    return render_template("Voronezh_Region.html")


@app.route("/Voronezh_Region_Nature")
def Voronezh_Region_Nature():
    return render_template("Voronezh_Region_Nature.html")


@app.route("/Donetsk_People_s_Republic")
def Donetsk_People_s_Republic():
    return render_template("Donetsk_People_s_Republic.html")


@app.route("/Donetsk_People_s_Republic_Nature")
def Donetsk_People_s_Republic_Nature():
    return render_template("Donetsk_People_s_Republic_Nature.html")


@app.route("/Jewish_JSC")
def Jewish_JSC():
    return render_template("Jewish_JSC.html")


@app.route("/Jewish_JSC_Nature")
def Jewish_JSC_Nature():
    return render_template("Jewish_JSC_Nature.html")


@app.route("/Trans_Baikal_Territory")
def Trans_Baikal_Territory():
    return render_template("Trans_Baikal_Territory.html")


@app.route("/Trans_Baikal_Territory_Nature")
def Trans_Baikal_Territory_Nature():
    return render_template("Trans_Baikal_Territory_Nature.html")


@app.route("/Zaporozhye_Region")
def Zaporozhye_Region():
    return render_template("Zaporozhye_Region.html")


@app.route("/Zaporozhye_Region_Nature")
def Zaporozhye_Region_Nature():
    return render_template("Zaporozhye_Region_Nature.html")


@app.route("/Ivanovo_Region")
def Ivanovo_Region():
    return render_template("Ivanovo_Region.html")


@app.route("/Irkutsk_Region")
def Irkutsk_Region():
    return render_template("Irkutsk_Region.html")


@app.route("/Irkutsk_Region_Nature")
def Irkutsk_Region_Nature():
    return render_template("Irkutsk_Region_Nature.html")


@app.route("/Kabardino_Balkarian_Republic")
def Kabardino_Balkarian_Republic():
    return render_template("Kabardino_Balkarian_Republic.html")


@app.route("/Kabardino_Balkarian_Republic_Nature")
def Kabardino_Balkarian_Republic_Nature():
    return render_template("Kabardino_Balkarian_Republic_Nature.html")


@app.route("/Kaliningrad_Region")
def Kaliningrad_Region():
    return render_template("Kaliningrad_Region.html")


@app.route("/Kaliningrad_Region_Nature")
def Kaliningrad_Region_Nature():
    return render_template("Kaliningrad_Region_Nature.html")


@app.route("/Kaluga_Region")
def Kaluga_Region():
    return render_template("Kaluga_Region.html")


@app.route("/Kaluga_Region_Nature")
def Kaluga_Region_Nature():
    return render_template("Kaluga_Region_Nature.html")


@app.route("/Kamchatka_Territory")
def Kamchatka_Territory():
    return render_template("Kamchatka_Territory.html")


@app.route("/Kamchatka_Territory_Nature")
def Kamchatka_Territory_Nature():
    return render_template("Kamchatka_Territory_Nature.html")


@app.route("/Karachay_Cherkess_Republic")
def Karachay_Cherkess_Republic():
    return render_template("Karachay_Cherkess_Republic.html")


@app.route("/Karachay_Cherkess_Republic_Nature")
def Karachay_Cherkess_Republic_Nature():
    return render_template("Karachay_Cherkess_Republic_Nature.html")


@app.route("/Kemerovo_Region")
def Kemerovo_Region():
    return render_template("Kemerovo_Region.html")


@app.route("/Kemerovo_Region_Nature")
def Kemerovo_Region_Nature():
    return render_template("Kemerovo_Region_Nature.html")


@app.route("/Kirov_Region")
def Kirov_Region():
    return render_template("Kirov_Region.html")


@app.route("/Kirov_Region_Nature")
def Kirov_Region_Nature():
    return render_template("Kirov_Region_Nature.html")


@app.route("/Kostroma_Region")
def Kostroma_Region():
    return render_template("Kostroma_Region.html")


@app.route("/Kostroma_Region_Nature")
def Kostroma_Region_Nature():
    return render_template("Kostroma_Region_Nature.html")


@app.route("/Krasnodarskiy_Territory")
def Krasnodarskiy_Territory():
    return render_template("Krasnodarskiy_Territory.html")


@app.route("/Krasnodarskiy_Territory_Nature")
def Krasnodarskiy_Territory_Nature():
    return render_template("Krasnodarskiy_Territory_Nature.html")


@app.route("/Krasnoyarsk_Territory")
def Krasnoyarsk_Territory():
    return render_template("Krasnoyarsk_Territory.html")


@app.route("/Krasnoyarsk_Territory_Nature")
def Krasnoyarsk_Territory_Nature():
    return render_template("Krasnoyarsk_Territory_Nature.html")


@app.route("/Kurgan_Region")
def Kurgan_Region():
    return render_template("Kurgan_Region.html")


@app.route("/Kurgan_Region_Nature")
def Kurgan_Region_Nature():
    return render_template("Kurgan_Region_Nature.html")


@app.route("/Kursk_Region")
def Kursk_Region():
    return render_template("Kursk_Region.html")


@app.route("/Kursk_Region_Nature")
def Kursk_Region_Nature():
    return render_template("Kursk_Region_Nature.html")


@app.route("/Leningrad_Region")
def Leningrad_Region():
    return render_template("Leningrad_Region.html")


@app.route("/Leningrad_Region_Nature")
def Leningrad_Region_Nature():
    return render_template("Leningrad_Region_Nature.html")


@app.route("/Lipetsk_Region")
def Lipetsk_Region():
    return render_template("Lipetsk_Region.html")


@app.route("/Lipetsk_Region_Nature")
def Lipetsk_Region_Nature():
    return render_template("Lipetsk_Region_Nature.html")


@app.route("/Luhansk_People_s_Republic")
def Luhansk_People_s_Republic():
    return render_template("Luhansk_People_s_Republic.html")


@app.route("/Luhansk_People_s_Republic_Nature")
def Luhansk_People_s_Republic_Nature():
    return render_template("Luhansk_People_s_Republic_Nature.html")


@app.route("/Magadan_Region")
def Magadan_Region():
    return render_template("Magadan_Region.html")


@app.route("/Magadan_Region_Nature")
def Magadan_Region_Nature():
    return render_template("Magadan_Region_Nature.html")


@app.route("/Moscow")
def Moscow():
    return render_template("Moscow.html")


@app.route("/Moscow_Nature")
def Moscow_Nature():
    return render_template("Moscow_Nature.html")


@app.route("/Moscow_Region")
def Moscow_Region():
    return render_template("Moscow_Region.html")


@app.route("/Moscow_Region_Nature")
def Moscow_Region_Nature():
    return render_template("Moscow_Region_Nature.html")


@app.route("/Murmansk_Region")
def Murmansk_Region():
    return render_template("Murmansk_Region.html")


@app.route("/Murmansk_Region_Nature")
def Murmansk_Region_Nature():
    return render_template("Murmansk_Region_Nature.html")


@app.route("/Nenets_AO")
def Nenets_AO():
    return render_template("Nenets_AO.html")


@app.route("/Nenets_AO_Nature")
def Nenets_AO_Nature():
    return render_template("Nenets_AO_Nature.html")


@app.route("/Nizhny_Novgorod_Region")
def Nizhny_Novgorod_Region():
    return render_template("Nizhny_Novgorod_Region.html")


@app.route("/Nizhny_Novgorod_Region_Nature")
def Nizhny_Novgorod_Region_Nature():
    return render_template("Nizhny_Novgorod_Region_Nature.html")


@app.route("/Novgorod_Region")
def Novgorod_Region():
    return render_template("Novgorod_Region.html")


@app.route("/Novgorod_Region_Nature")
def Novgorod_Region_Nature():
    return render_template("Novgorod_Region_Nature.html")


@app.route("/Novosibirsk_Region")
def Novosibirsk_Region():
    return render_template("Novosibirsk_Region.html")


@app.route("/Novosibirsk_Region_Nature")
def Novosibirsk_Region_Nature():
    return render_template("Novosibirsk_Region_Nature.html")


@app.route("/Omsk_Region")
def Omsk_Region():
    return render_template("Omsk_Region.html")


@app.route("/Omsk_Region_Nature")
def Omsk_Region_Nature():
    return render_template("Omsk_Region_Nature.html")


@app.route("/Orenburg_Region")
def Orenburg_Region():
    return render_template("Orenburg_Region.html")


@app.route("/Orenburg_Region_Nature")
def Orenburg_Region_Nature():
    return render_template("Orenburg_Region_Nature.html")


@app.route("/Oryol_Region")
def Oryol_Region():
    return render_template("Oryol_Region.html")


@app.route("/Oryol_Region_Nature")
def Oryol_Region_Nature():
    return render_template("Oryol_Region_Nature.html")


@app.route("/Penza_Region")
def Penza_Region():
    return render_template("Penza_Region.html")


@app.route("/Penza_Region_Nature")
def Penza_Region_Nature():
    return render_template("Penza_Region_Nature.html")


@app.route("/Perm_Territory")
def Perm_Territory():
    return render_template("Perm_Territory.html")


@app.route("/Perm_Territory_Nature")
def Perm_Territory_Nature():
    return render_template("Perm_Territory_Nature.html")


@app.route("/Primorsky_Territory")
def Primorsky_Territory():
    return render_template("Primorsky_Territory.html")


@app.route("/Primorsky_Territory_Nature")
def Primorsky_Territory_Nature():
    return render_template("Primorsky_Territory_Nature.html")


@app.route("/Pskov_Region")
def Pskov_Region():
    return render_template("Pskov_Region.html")


@app.route("/Pskov_Region_Nature")
def Pskov_Region_Nature():
    return render_template("Pskov_Region_Nature.html")


@app.route("/Republic_of_Adygea")
def Republic_of_Adygea():
    return render_template("Republic_of_Adygea.html")


@app.route("/Republic_of_Adygea_Nature")
def Republic_of_Adygea_Nature():
    return render_template("Republic_of_Adygea_Nature.html")


@app.route("/Republic_of_Altai")
def Republic_of_Altai():
    return render_template("Republic_of_Altai.html")


@app.route("/Republic_of_Altai_Nature")
def Republic_of_Altai_Nature():
    return render_template("Republic_of_Altai_Nature.html")


@app.route("/Republic_of_Bashkortostan")
def Republic_of_Bashkortostan():
    return render_template("Republic_of_Bashkortostan.html")


@app.route("/Republic_of_Bashkortostan_Nature")
def Republic_of_Bashkortostan_Nature():
    return render_template("Republic_of_Bashkortostan_Nature.html")


@app.route("/Republic_of_Buryatia")
def Republic_of_Buryatia():
    return render_template("Republic_of_Buryatia.html")


@app.route("/Republic_of_Buryatia_Nature")
def Republic_of_Buryatia_Nature():
    return render_template("Republic_of_Buryatia_Nature.html")


@app.route("/Republic_of_Dagestan")
def Republic_of_Dagestan():
    return render_template("Republic_of_Dagestan.html")


@app.route("/Republic_of_Dagestan_Nature")
def Republic_of_Dagestan_Nature():
    return render_template("Republic_of_Dagestan_Nature.html")


@app.route("/Republic_of_Ingushetia")
def Republic_of_Ingushetia():
    return render_template("Republic_of_Ingushetia.html")


@app.route("/Republic_of_Ingushetia_Nature")
def Republic_of_Ingushetia_Nature():
    return render_template("Republic_of_Ingushetia_Nature.html")


@app.route("/Republic_of_Kalmykia")
def Republic_of_Kalmykia():
    return render_template("Republic_of_Kalmykia.html")


@app.route("/Republic_of_Kalmykia_Nature")
def Republic_of_Kalmykia_Nature():
    return render_template("Republic_of_Kalmykia_Nature.html")


@app.route("/Republic_of_Karelia")
def Republic_of_Karelia():
    return render_template("Republic_of_Karelia.html")


@app.route("/Republic_of_Karelia_Nature")
def Republic_of_Karelia_Nature():
    return render_template("Republic_of_Karelia_Nature.html")


@app.route("/Republic_of_Komi")
def Republic_of_Komi():
    return render_template("Republic_of_Komi.html")


@app.route("/Republic_of_Komi_Nature")
def Republic_of_Komi_Nature():
    return render_template("Republic_of_Komi_Nature.html")


@app.route("/Republic_of_Crimea")
def Republic_of_Crimea():
    return render_template("Republic_of_Crimea.html")


@app.route("/Republic_of_Crimea_Nature")
def Republic_of_Crimea_Nature():
    return render_template("Republic_of_Crimea_Nature.html")


@app.route("/Republic_of_Mari_El")
def Republic_of_Mari_El():
    return render_template("Republic_of_Mari_El.html")


@app.route("/Republic_of_Mari_El_Nature")
def Republic_of_Mari_El_Nature():
    return render_template("Republic_of_Mari_El_Nature.html")


@app.route("/Republic_of_Mordovia")
def Republic_of_Mordovia():
    return render_template("Republic_of_Mordovia.html")


@app.route("/Republic_of_Mordovia_Nature")
def Republic_of_Mordovia_Nature():
    return render_template("Republic_of_Mordovia_Nature.html")


@app.route("/Republic_of_Sakha")
def Republic_of_Sakha():
    return render_template("Republic_of_Sakha.html")


@app.route("/Republic_of_Sakha_Nature")
def Republic_of_Sakha_Nature():
    return render_template("Republic_of_Sakha_Nature.html")


@app.route("/Republic_of_North_Ossetia_Alania")
def Republic_of_North_Ossetia_Alania():
    return render_template("Republic_of_North_Ossetia_Alania.html")


@app.route("/Republic_of_North_Ossetia_Alania_Nature")
def Republic_of_North_Ossetia_Alania_Nature():
    return render_template("Republic_of_North_Ossetia_Alania_Nature.html")


@app.route("/Republic_of_Tatarstan")
def Republic_of_Tatarstan():
    return render_template("Republic_of_Tatarstan.html")


@app.route("/Republic_of_Tatarstan_Nature")
def Republic_of_Tatarstan_Nature():
    return render_template("Republic_of_Tatarstan_Nature.html")


@app.route("/Republic_of_Tyva")
def Republic_of_Tyva():
    return render_template("Republic_of_Tyva.html")


@app.route("/Republic_of_Tyva_Nature")
def Republic_of_Tyva_Nature():
    return render_template("Republic_of_Tyva_Nature.html")


@app.route("/Republic_of_Khakassia")
def Republic_of_Khakassia():
    return render_template("Republic_of_Khakassia.html")


@app.route("/Republic_of_Khakassia_Nature")
def Republic_of_Khakassia_Nature():
    return render_template("Republic_of_Khakassia_Nature.html")


@app.route("/Rostov_Region")
def Rostov_Region():
    return render_template("Rostov_Region.html")


@app.route("/Rostov_Region_Nature")
def Rostov_Region_Nature():
    return render_template("Rostov_Region_Nature.html")


@app.route("/Ryazan_Region")
def Ryazan_Region():
    return render_template("Ryazan_Region.html")


@app.route("/Ryazan_Region_Nature")
def Ryazan_Region_Nature():
    return render_template("Ryazan_Region_Nature.html")


@app.route("/Samara_Region")
def Samara_Region():
    return render_template("Samara_Region.html")


@app.route("/Samara_Region_Nature")
def Samara_Region_Nature():
    return render_template("Samara_Region_Nature.html")


@app.route("/Saint_Petersburg")
def Saint_Petersburg():
    return render_template("Saint_Petersburg.html")


@app.route("/Saint_Petersburg_Nature")
def Saint_Petersburg_Nature():
    return render_template("Saint_Petersburg_Nature.html")


@app.route("/Saratov_Region")
def Saratov_Region():
    return render_template("Saratov_Region.html")


@app.route("/Saratov_Region_Nature")
def Saratov_Region_Nature():
    return render_template("Saratov_Region_Nature.html")


@app.route("/Sakhalin_Region")
def Sakhalin_Region():
    return render_template("Sakhalin_Region.html")


@app.route("/Sakhalin_Region_Nature")
def Sakhalin_Region_Nature():
    return render_template("Sakhalin_Region_Nature.html")


@app.route("/Sverdlovsk_Region")
def Sverdlovsk_Region():
    return render_template("Sverdlovsk_Region.html")


@app.route("/Sverdlovsk_Region_Nature")
def Sverdlovsk_Region_Nature():
    return render_template("Sverdlovsk_Region_Nature.html")


@app.route("/Sevastopol")
def Sevastopol():
    return render_template("Sevastopol.html")


@app.route("/Sevastopol_Nature")
def Sevastopol_Nature():
    return render_template("Sevastopol_Nature.html")


@app.route("/Smolensk_Region")
def Smolensk_Region():
    return render_template("Smolensk_Region.html")


@app.route("/Smolensk_Region_Nature")
def Smolensk_Region_Nature():
    return render_template("Smolensk_Region_Nature.html")


@app.route("/Stavropol_Territory")
def Stavropol_Territory():
    return render_template("Stavropol_Territory.html")


@app.route("/Stavropol_Territory_Nature")
def Stavropol_Territory_Nature():
    return render_template("Stavropol_Territory_Nature.html")


@app.route("/Tambov_Region")
def Tambov_Region():
    return render_template("Tambov_Region.html")


@app.route("/Tambov_Region_Nature")
def Tambov_Region_Nature():
    return render_template("Tambov_Region_Nature.html")


@app.route("/Tver_Region")
def Tver_Region():
    return render_template("Tver_Region.html")


@app.route("/Tver_Region_Nature")
def Tver_Region_Nature():
    return render_template("Tver_Region_Nature.html")


@app.route("/Tomsk_Region")
def Tomsk_Region():
    return render_template("Tomsk_Region.html")


@app.route("/Tomsk_Region_Nature")
def Tomsk_Region_Nature():
    return render_template("Tomsk_Region_Nature.html")


@app.route("/Tula_Region")
def Tula_Region():
    return render_template("Tula_Region.html")


@app.route("/Tula_Region_Nature")
def Tula_Region_Nature():
    return render_template("Tula_Region_Nature.html")


@app.route("/Tyumen_Region")
def Tyumen_Region():
    return render_template("Tyumen_Region.html")


@app.route("/Tyumen_Region_Nature")
def Tyumen_Region_Nature():
    return render_template("Tyumen_Region_Nature.html")


@app.route("/Udmurt_Republic")
def Udmurt_Republic():
    return render_template("Udmurt_Republic.html")


@app.route("/Udmurt_Republic_Nature")
def Udmurt_Republic_Nature():
    return render_template("Udmurt_Republic_Nature.html")


@app.route("/Ulyanovsk_Region")
def Ulyanovsk_Region():
    return render_template("Ulyanovsk_Region.html")


@app.route("/Ulyanovsk_Region_Nature")
def Ulyanovsk_Region_Nature():
    return render_template("Ulyanovsk_Region_Nature.html")


@app.route("/Khabarovsk_Territory")
def Khabarovsk_Territory():
    return render_template("Khabarovsk_Territory.html")


@app.route("/Khabarovsk_Territory_Nature")
def Khabarovsk_Territory_Nature():
    return render_template("Khabarovsk_Territory_Nature.html")


@app.route("/Khanty_Mansiysk_JSC")
def Khanty_Mansiysk_JSC():
    return render_template("Khanty_Mansiysk_JSC.html")


@app.route("/Khanty_Mansiysk_JSC_Nature")
def Khanty_Mansiysk_JSC_Nature():
    return render_template("Khanty_Mansiysk_JSC_Nature.html")


@app.route("/Kherson_Region")
def Kherson_Region():
    return render_template("Kherson_Region.html")


@app.route("/Kherson_Region_Nature")
def Kherson_Region_Nature():
    return render_template("Kherson_Region_Nature.html")


@app.route("/Chelyabinsk_Region")
def Chelyabinsk_Region():
    return render_template("Chelyabinsk_Region.html")


@app.route("/Chelyabinsk_Region_Nature")
def Chelyabinsk_Region_Nature():
    return render_template("Chelyabinsk_Region_Nature.html")


@app.route("/Chechen_Republic")
def Chechen_Republic():
    return render_template("Chechen_Republic.html")


@app.route("/Chechen_Republic_Nature")
def Chechen_Republic_Nature():
    return render_template("Chechen_Republic_Nature.html")


@app.route("/Chuvash_Republic")
def Chuvash_Republic():
    return render_template("Chuvash_Republic.html")


@app.route("/Chuvash_Republic_Nature")
def Chuvash_Republic_Nature():
    return render_template("Chuvash_Republic_Nature.html")


@app.route("/Chukotsiy_JSC")
def Chukotsiy_JSC():
    return render_template("Chukotsiy_JSC.html")


@app.route("/Chukotsiy_JSC_Nature")
def Chukotsiy_JSC_Nature():
    return render_template("Chukotsiy_JSC_Nature.html")


@app.route("/Yamalo_Nenets_JSC")
def Yamalo_Nenets_JSC():
    return render_template("Yamalo_Nenets_JSC.html")


@app.route("/Yamalo_Nenets_JSC_Nature")
def Yamalo_Nenets_JSC_Nature():
    return render_template("Yamalo_Nenets_JSC_Nature.html")


@app.route("/Yaroslavl_Region")
def Yaroslavl_Region():
    return render_template("Yaroslavl_Region.html")


@app.route("/Yaroslavl_Region_Nature")
def Yaroslavl_Region_Nature():
    return render_template("Yaroslavl_Region_Nature.html")


# Страница Театров
@app.route("/Theaters_of_the_RF")
def Theaters_of_the_RF():
    session = db_session.create_session()
    theater = session.query(Theater).all()
    return render_template("Theaters_of_the_RF.html", theater=theater)


# Страница кинотеатров
@app.route("/Cinema_RF")
def Cinema_RF():
    session = db_session.create_session()
    cinema = session.query(Movie).all()
    return render_template("Cinema_RF.html", cinema=cinema)


#Страница заповедников
@app.route("/nature_reserves")
def nature_reserves():
    return render_template("nature_reserves.html")


#Животные
@app.route("/animals")
def animals():
    return render_template("animals.html")


#Насекомоядные
@app.route("/insectivores")
def insectivores():
    return render_template("insectivores.html")


#Рукокрылые
@app.route("/bats")
def bats():
    return render_template("bats.html")


#Грызуны
@app.route("/rodents")
def rodents():
    return render_template("rodents.html")


#Хищные + Псовые
@app.route("/predatory")
def predatory():
    return render_template("predatory.html")


#Медвежьи
@app.route("/bearish")
def bearish():
    return render_template("bearish.html")


#Куньи
@app.route("/mustelidae")
def mustelidae():
    return render_template("mustelidae.html")


#Кошачьи
@app.route("/feline")
def feline():
    return render_template("feline.html")


#Гиеновые
@app.route("/hyena")
def hyena():
    return render_template("hyena.html")


#Ластоногие
@app.route("/pinnipeds")
def pinnipeds():
    return render_template("pinnipeds.html")


#Непарнокопытные
@app.route("/ungulates")
def ungulates():
    return render_template("ungulates.html")


#Жвачные
@app.route("/ruminats")
def ruminats():
    return render_template("ruminats.html")


#Китообразные
@app.route("/cetaceans")
def cetaceans():
    return render_template("cetaceans.html")


#Plants
@app.route("/plants")
def plants():
    return render_template("plants.html")


if __name__ == '__main__':
    db_session.global_init('db/tourism.db')
    app.run()