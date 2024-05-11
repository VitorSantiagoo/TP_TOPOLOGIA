import smtplib

servidor_email = smtplib.SMTP('smtp.gmail.com',587)

servidor_email.starttls()

servidor_email.login("vitor123452005@gmail.com", "")

remetente = "vitor123452005@gmail.com"
destinatarios = "gleison.batista@prozeducacao.com.br"

conteudo = "Fala gleissin, Tmj!"

servidor_email.sendmail(remetente, destinatarios, conteudo)

servidor_email.quit