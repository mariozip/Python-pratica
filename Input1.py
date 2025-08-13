def ricevi_input_utente() -> str:
  """
  Chiede all'utente di inserire del testo e lo restituisce.
  """
  # Chiede all'utente di inserire qualcosa
  return input("Ciao! Per favore, inserisci del testo: ")

# Esempio di come chiamare la funzione
if __name__ == "__main__":
  # La funzione viene chiamata e il suo risultato viene passato direttamente a print()
  input_ricevuto = ricevi_input_utente()
  print(f"Hai inserito: {input_ricevuto}")
