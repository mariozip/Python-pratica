def ricevi_input_utente() -> str:
  """
  Chiede all'utente di inserire del testo e lo restituisce come stringa.
  """
  # Chiede all'utente di inserire qualcosa
  testo_inserito: str = input("Ciao! Per favore, inserisci del testo: ")

  # Mostra all'utente cosa ha inserito
  print(f"Hai inserito: {testo_inserito}")

  # Restituisce il valore inserito, così può essere usato altrove
  return testo_inserito

# Esempio di come chiamare la funzione
if __name__ == "__main__":
  input_ricevuto: str = ricevi_input_utente()

  # Mostra all'utente cosa ha inserito
  print(f"Hai inserito: {input_ricevuto}")

  # Ora puoi usare la variabile 'input_ricevuto' per altre operazioni
  print(f"La funzione ha restituito: {input_ricevuto}")
