
from pyscript import display, document

def create_order(e):
    document.getElementById('output').innerHTML = "  "
    document.getElementById('output2').innerHTML = "  "

    m1 = int(document.getElementById("menu1").value)
    m2 = int(document.getElementById("menu2").value)
    m3 = int(document.getElementById("menu3").value)

    total = m1 + m2 + m3
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    phone = document.getElementById("hollanumba").value

    result = f'Customer: {name}  ({phone})  at {address}'
    
    display(f'{result}', target='output')
    display(f'total price: {total} PHP', target='output2')