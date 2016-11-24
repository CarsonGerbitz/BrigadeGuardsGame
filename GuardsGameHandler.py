def GuardsGameHandler():
    def Setup():
        import CharSetup, HstlSetup
        CharSetup.CharSelect()
        HstlSetup
    def Start():
        import Battle
        Battle
    Setup()
    Start()
GuardsGameHandler()
