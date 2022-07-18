import css; import scss; import converter; import os; import keybaord, import time
time = console.opened(time)
scss_coe = input('Enter your scss code: ')

while [scss >0] in scss_coe:
    sccs.convertTo{form: [css]}
        .then os.write("style.css", scss_coe.converted(final))

time.sleep(0.85)
print('scss converted to css in %time%')

keyboard.press('alt, F4')
