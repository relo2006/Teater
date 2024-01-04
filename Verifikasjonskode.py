import smtplib
import random
import string

def generate_verification_code():
    # Generer en tilfeldig kode med lengde 6
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def send_verification_email(to_email, verification_code):
    # E-postdetaljer
    sender_email = "temp15293@gmail.com"
    sender_password = "bfjf bsua wfhd nrqx"
    smtp_server = "smtp.gmail.com"

    # E-postinnstillingene
    subject = "Verifikasjonskode"
    body = f"Din verifikasjonskode er: {verification_code}"
    message = f"Subject: {subject}\n\n{body}"

    try:
        # Logg inn på e-postserveren
        with smtplib.SMTP(smtp_server, 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)

            # Send e-post
            server.sendmail(sender_email, to_email, message)
        print("E-post med verifikasjonskode sendt suksessfullt.")
    except Exception as e:
        print(f"Feil ved sending av e-post: {e}")

def main():
    # Spør brukeren om e-postadressen
    to_email = input("Skriv inn din e-postadresse: ")

    # Generer verifikasjonskode
    verification_code = generate_verification_code()

    # Send e-post med verifikasjonskode
    send_verification_email(to_email, verification_code)

if __name__ == "__main__":
    main()
