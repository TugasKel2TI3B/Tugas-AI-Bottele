# mengimport package pyTelegramBotAPI
import telebot

# inisialisasi Token Bot Kita
bot = telebot.TeleBot('5877873866:AAEgh7azx01HqVl5slhr9FLh_mQDY-OV47U')

# Menghandle Pesan /start
@bot.message_handler(commands=['start'])
def welcome(message):
    # membalas pesan
    bot.reply_to(message, 'Halo, Selamat datang di bot Politeknik Purbaya. Tentang kampus kami bisa Anda liat di IG: poltek.purbaya. Jelajahi bot kami, siapkan masa depanmu dan daftarkan dirimu di Politeknik Purbaya')

# Menghandle Pesan /help
@bot.message_handler(commands=['help'])
def welcome(message):
    # membalas pesan
    bot.reply_to(message, 'Anda bisa menunggu balasan kami pada jam kerja senin-sabtu pukul 08.00-20.00 WIB')

# Menghandle Pesan /about
@bot.message_handler(commands=['about'])
def welcome(message):
    # membalas pesan
    bot.reply_to(message, 'Politeknik Purbaya yaitu memiliki 2 kampus, kampus 1 berada di jl.pancakarya No.1, Kalimati, Kajen, kec. Talang, kab. Tegal, Jawa tengah. Kampus 2 berada di jl. Supriyadi, Trayeman, kec.Slawi, kab. Tegal, Jawa tengah. Yang berakreditasi b dengan 2 pilihan jurusan, yaitu TI dan TM')
    
while True:
    try:
        bot.polling()
    except:
        pass