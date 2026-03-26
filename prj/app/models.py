from django.db import models


class Znacka(models.Model):
    nazev = models.CharField(max_length=100)

    def __str__(self):
        return self.nazev


class Model(models.Model):
    nazev = models.CharField(max_length=100)
    znacka = models.ForeignKey(Znacka, on_delete=models.CASCADE)

    def __str__(self):
        return self.nazev


class Auto(models.Model):
    nazev = models.CharField(max_length=100)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)

    def __str__(self):
        return self.nazev


class Motorizace(models.Model):
    typ = models.CharField(max_length=100)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)

    def __str__(self):
        return self.typ


class Uzivatel(models.Model):
    jmeno = models.CharField(max_length=100)

    def __str__(self):
        return self.jmeno


class Recenze(models.Model):
    text = models.TextField()
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)

    def __str__(self):
        return f"Recenze {self.id}"


class Komentar(models.Model):
    text = models.TextField()
    recenze = models.ForeignKey(Recenze, on_delete=models.CASCADE)

    def __str__(self):
        return f"Komentar {self.id}"


class Hodnoceni(models.Model):
    hodnota = models.IntegerField()
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    uzivatel = models.ForeignKey(Uzivatel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.hodnota)
e=models.CASCADE)
