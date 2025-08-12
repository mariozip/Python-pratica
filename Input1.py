def ricevi_input_utente():
  """
  Questa procedura chiede all'utente di inserire del testo,
  lo stampa a schermo e lo restituisce come stringa.
  """
  # Chiede all'utente di inserire qualcosa
  testo_inserito = input("Ciao! Per favore, inserisci del testo: ")

  # Mostra all'utente cosa ha inserito
  print(f"Hai inserito: {testo_inserito}")

  # Restituisce il valore inserito, così può essere usato altrove
  return testo_inserito

# Esempio di come chiamare la procedura
if __name__ == "__main__":
  input_ricevuto = ricevi_input_utente()
  # Ora puoi usare la variabile 'input_ricevuto' per altre operazioni
  print(f"La procedura ha restituito: {input_ricevuto}")
