import time
import flet as ft
import model as md
from view import View


#la mia Class SpellChecker

class SpellChecker:

    def __init__(self, v: View):
        self._multiDic = md.MultiDictionary()
        self._view = v


    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    def handleVerificaLingua(self, e):
        self._view._txtOut.controls.append(ft.Text(value="Language correctly selected: " + self._view._ddLingua.value))
        self._view.update()

    def handleVerificaTipoRicerca(self, e):
        self._view._txtOut.controls.append(ft.Text(value="Modality correctly selected: " + self._view._ddTipoRicerca.value))
        self._view.update()

    def handleSpellCheck(self, e):
        frase = self._view._txtIn.value
        if frase == "":
            self._view._txtOut.controls.clear()
            self._view._txtOut.controls.append(ft.Text(value="Attention. Add a sentence"))
            self._view.update()
            return

        lingua = self._view._ddLingua.value
        if lingua is None:
            self._view._txtOut.controls.clear()
            self._view._txtOut.controls.append(ft.Text(value="Attention. Select the language"))
            self._view._txtIn.value = ""
            self._view.update()
            return
        print(lingua)

        modalita = self._view._ddTipoRicerca.value
        if modalita is None:
            self._view._txtOut.controls.clear()
            self._view._txtOut.controls.append(ft.Text(value="Attention. Select the modality"))
            self._view._txtIn.value = ""
            self._view.update()
            return
        print(modalita)

        parole, elapsedTime = self.handleSentence(frase, lingua, modalita)
        self._view._txtOut.controls.clear()
        self._view._txtOut.controls.append(ft.Text("Frase inserita: " + frase))
        self._view._txtOut.controls.append(ft.Text("Parole errate: " + parole))
        self._view._txtOut.controls.append(ft.Text(value="Tempo richiesto dalla ricerca: " + str(elapsedTime)))

        self._view._txtIn.value = ""
        self._view.update()
def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text