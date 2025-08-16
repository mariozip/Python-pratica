# per eseguire digitare nel terminal:
# streamlit run /workspaces/Python-pratica/app_streamlit.py
# streamlit run /workspaces/Python-pratica/app_streamlit.py &   // così lo esegue in background e il terminal rimane a


import streamlit as st

# Definiamo le opzioni come una costante per una migliore organizzazione
OPZIONI_PROFESSIONE = ["Seleziona...", "Studente", "Ingegnere", "Medico", "Artista", "Altro"]

def valida_input(nome, cognome, eta, professione):
    """
    Valida i dati di input del form e restituisce una lista di errori.
    """
    errori = []
    if not nome:
        errori.append("Il campo 'Nome' è obbligatorio.")
    if not cognome:
        errori.append("Il campo 'Cognome' è obbligatorio.")
    if eta <= 0:
        errori.append("L'età deve essere un numero maggiore di zero.")
    if professione == "Seleziona...":
        errori.append("Devi selezionare una professione.")
    return errori

def mostra_dati_inviati(nome, cognome, eta, professione, note):
    st.write(f"**Nome completo:** {nome} {cognome}")
    st.write(f"**Età:** {eta} anni")
    st.write(f"**Professione:** {professione}")
    if note:
        st.write(f"**Note:** {note}")

def main():
    """
    Funzione principale che definisce e gestisce l'interfaccia dell'app Streamlit.
    """
    # st.title() crea un titolo grande per la nostra "pagina" web
    st.title("Modulo di Inserimento Dati")

    # st.form crea un contenitore per raggruppare più elementi di input.
    # L'app non si riavvia ad ogni interazione con un widget all'interno del form.
    with st.form("user_form"):
        st.header("Inserisci le tue informazioni")

        # st.columns crea un layout a colonne.
        # Lo usiamo per affiancare i campi Nome e Cognome.
        col1, col2 = st.columns(2)
        with col1:
            nome = st.text_input("Nome")
        with col2:
            cognome = st.text_input("Cognome")

        eta = st.number_input("Età", min_value=0, max_value=120, step=1)
        
        # st.selectbox crea un menu a tendina.
        # Il primo argomento è l'etichetta, il secondo è la lista di opzioni.
        # Aggiungiamo un'opzione iniziale per assicurarci che l'utente faccia una scelta attiva.
        professione = st.selectbox("Professione", OPZIONI_PROFESSIONE)

        # st.text_area crea un campo di testo su più righe.
        note = st.text_area("Note aggiuntive (opzionale)")

        # st.form_submit_button è un pulsante speciale per i form.
        # Quando viene cliccato, invia tutti i dati del form in una volta.
        submitted = st.form_submit_button("Invia Dati")

        if submitted:
            errori = valida_input(nome, cognome, eta, professione)

            if not errori:
                st.success(f"Dati ricevuti con successo!")
                # Usiamo un expander per mostrare i dati inviati in modo ordinato
                with st.expander("Visualizza i dati inviati"):
                    mostra_dati_inviati(nome, cognome, eta, professione, note)
            else:
                for errore in errori:
                    st.error(errore)

# Questo blocco viene eseguito solo quando lo script è avviato direttamente.
if __name__ == "__main__":
    main()
