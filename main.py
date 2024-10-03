import curses, random
from curses import wrapper

option = ("gunting", "batu", "kertas")

def main(stdscr):
    # game = True membuat loop permainan berulang hingga pemain memutuskan untuk keluar
    game = True
    while game:
        # Membersihkan layar terminal setiap kali loop dimulai
        stdscr.clear()
        
        # Komputer memilih pilihannya
        computer = random.choice(option)
        
        stdscr.addstr("Ini adalah game gunting batu kertas!\n")
        stdscr.addstr("1. Gunting\n")
        stdscr.addstr("2. Batu\n")
        stdscr.addstr("3. Kertas\n")
        stdscr.addstr("Pilih gacok mu! = \n")
        
        # Player memilih pilihannya dan dimasukkan ke variabel playerChoice
        player = stdscr.getkey()
        playerChoice = None
        
        # Mengganti input pemain menjadi pilihan yang benar sesuai dengan pilihan yang ada
        if player == "1":
            playerChoice = option[0]
        elif player == "2":
            playerChoice = option[1]
        elif player == "3":
            playerChoice = option[2]
        else:
            # Jika input tidak valid, menampilkan pesan error dan memulai kembali
            stdscr.addstr("\nInput salah! Masukkan input yang benar!\n")
            stdscr.refresh()
            stdscr.getch()
            continue
        
        # Menampilkan pilihan pemain dan komputer
        stdscr.addstr(f"\nPilihannmu   : {playerChoice}\n")
        stdscr.addstr(f"Komputer     : {computer}\n")

        # Menentukan hasil permainan berdasarkan aturan permainan batu-gunting-kertas
        if playerChoice == computer:
            result = "Seri!"
            # Seri jika pilihan sama
        elif (playerChoice == "gunting" and computer == "kertas") or \
             (playerChoice == "batu" and computer == "gunting") or \
             (playerChoice == "kertas" and computer == "batu"):
            result = "Kamu menang!"
            # Pemain menang jika mengikuti aturan yang benar
        else:
            result = "Skill issue"
            # Komputer menang
        
        # Menampilkan hasil pertandingan
        stdscr.addstr(f"\nResult: {result}\n")
        # Instruksi lanjut atau keluar
        stdscr.addstr("\nTekan tombol apapun untuk bermain lagi!\n")
        stdscr.addstr("Atau tekan tombol 'q' untuk keluar dari permainan!")
        stdscr.refresh()

        # Menunggu input pengguna untuk melanjutkan atau keluar
        stdscr.nodelay(False)

        key = stdscr.getkey()
        if key == "q":
            game = False
            # Menghentikan permainan jika pemain menekan 'q'

wrapper(main)
