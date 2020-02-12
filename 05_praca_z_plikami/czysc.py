"""
otwórz plik z e-mailami (emaile.txt), 
odczytaj go. wypisz na ekranie przeczyszczone, unikalne emaile

przyjmij nazwe pliku jako parametr w command line - czyli jako parametr dla pythona
obsłuż sytuację gdy użytkownik nie poda tej nazwy
obsłuż sytuację gdy podana jest nazwa nieistniejącego pliku

Dołóż drugi - opcjonalny parametr - plik wynikowy
"""
import sys

def clean_email(text):
    text = text.strip().lower()
    if text.count("@") == 1:
        return text

def main(file_name):
    with open(file_name) as f:
        #print(f.read().splitlines())
        cleaned_emails = set()
        for line in f:
            email = clean_email(line)
            if email:
                cleaned_emails.add(email)

    cleaned_emails = sorted(cleaned_emails)
    print("\n".join(cleaned_emails))
    return("\n".join(cleaned_emails))


try:
    main(sys.argv[1])
except IndexError:
    print("Nie podałeś pliku wsadowego. Podaj nazwę (i ścieżkę) pliku")
except FileNotFoundError:
    print("Nie ma takiego pliku. Podaj prawidłową nazwę (i ścieżkę) pliku")

try:
    with open(sys.argv[2], 'w') as f:
        f.write(main(sys.argv[1]))
        print(f"Pomyślnie zapisano w pliku {sys.argv[2]}")
except IndexError:
    print("Nie podano pliku wyjściowego. Jeśli chcesz zapisać wynik - podaj nazwę pliku")