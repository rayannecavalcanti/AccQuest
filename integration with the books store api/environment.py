def before_scenario(context, scenario):
    print(f"Executando cenário: {scenario.name}")

def after_scenario(context, scenario):
    print(f"Cenário concluído: {scenario.name}")