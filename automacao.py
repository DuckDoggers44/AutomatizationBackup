import pyautogui
import time 

pyautogui.alert('O código irá começar, não mexa no teclado ou mouse pois isso afetará a execução do código')
pyautogui.PAUSE = 0.5

# Abrir google drive no meu computador
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(5)
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')

# Entrar na minha área de trabalho 
pyautogui.hotkey('winleft', 'd')

# Clicar no arquivo que eu quero fazer backup e arrastar ele 
pyautogui.moveTo(332, 239)
pyautogui.mouseDown()

# Enquanto eu estiver arrastando o arquivo, mudo a tela para o drive na minha pasta e solto, após isso fecho o site.
pyautogui.moveTo(1138, 277)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.moveTo(1149, 254)
time.sleep(2)
pyautogui.mouseUp()
time.sleep(5)
pyautogui.hotkey('alt', 'f4')

pyautogui.alert('O código acabou de executar. Pode usar seu computador agora!')

# Descobrir a posição que o mouse precisa estar para (clicar,arrastar,selecionar) realizar a função desejada.

# Aqui apartir da necessidade de espera do seu computador você irá colocar os segundos que precisa. (só tirar as # e rodar o código)
# time.sleep()
# pyautogui.position()

# Executar comando de posição e colocar no código pyautogui.moveto após isso só rodar o programa.



# OBS: Eu fiz esse código seguindo as necessidades que eu tinha, como colocar o arquivo em uma pasta específica 
# e calcular o tempo necessário para meu navegador entrar no site. Você pode personalizar com base na sua realidade.