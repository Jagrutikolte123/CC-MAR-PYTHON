import tkinter as tk
import smtplib

def send_mail():
    email_address = email_entry.get()
    password = password_entry.get()
    recipient = recipient_entry.get()
    subject = subject_entry.get()
    body = body_text.get('1.0', tk.END)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(email_address, password)

            message = f'Subject: {subject}\n\n{body}'

            smtp.sendmail(email_address, recipient, message)

        status_label.config(text='Mail sent successfully!', fg='green')
    except:
        status_label.config(text='Mail failed to send.', fg='red')

root = tk.Tk()
root.title('Mail Application')

email_label = tk.Label(root, text='Email Address')
email_label.grid(row=0, column=0)

email_entry = tk.Entry(root)
email_entry.grid(row=0, column=1)

password_label = tk.Label(root, text='Password')
password_label.grid(row=1, column=0)

password_entry = tk.Entry(root, show='*')
password_entry.grid(row=1, column=1)

recipient_label = tk.Label(root, text='Recipient')
recipient_label.grid(row=2, column=0)

recipient_entry = tk.Entry(root)
recipient_entry.grid(row=2, column=1)

subject_label = tk.Label(root, text='Subject')
subject_label.grid(row=3, column=0)

subject_entry = tk.Entry(root)
subject_entry.grid(row=3, column=1)

body_label = tk.Label(root, text='Body')
body_label.grid(row=4, column=0)

body_text = tk.Text(root)
body_text.grid(row=4, column=1)

send_button = tk.Button(root, text='Send', command=send_mail)
send_button.grid(row=5, column=1)

status_label = tk.Label(root, text='')
status_label.grid(row=6, column=1)

root.mainloop()
