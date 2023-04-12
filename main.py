print("Bem vindo à Loja de Tintas do seu ZÉ")
metros_quadrados = input("Qual a área em m²?\n")
metros_quadrados = float(metros_quadrados)

# Coloque o código para resolver o problema nessa parte do programa
Cobertura_da_tinta = 3
litros_por_lata = 18
preço_da_tinta = 80
Cobertura_da_lata = int(Cobertura_da_tinta * litros_por_lata)
litros_necessários = (metros_quadrados/Cobertura_da_tinta)
if litros_necessários <= 18:
    qtd_de_latas = 1
else:
    qtd_de_latas = int(litros_necessários/litros_por_lata)
    if litros_necessários % litros_por_lata !=0:
        qtd_de_latas += 1 



# As duas variáveis qtd_de_latas e valor_total devem guardar a resposta do problema
# Troque os zeros pelos valores corretos.
valor_total = qtd_de_latas * 80

print(f"Serão necessárias {qtd_de_latas} latas totalizando R$ {valor_total}")