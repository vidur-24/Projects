const form = document.querySelector('form');
const inTemp = document.querySelector('#inTemp');
const outTemp = document.querySelector('#outTemp');
const inUnit = document.querySelector('#inUnit');
const outUnit = document.querySelector('#outUnit');
const submitBtn = document.querySelector('#convert');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    if(inTemp.value === '') {
        alert('Please enter the temperature');
        return;
    }

    if (inUnit.value === outUnit.value) {
        outTemp.value = inTemp.value;
    }
    else{
        if (inUnit.value === 'c' && outUnit.value === 'f') { // c->f
            outTemp.value = (parseFloat(inTemp.value) * 9 / 5) + 32;
        } 
        else if (inUnit.value === 'f' && outUnit.value === 'c') { // f->c
            outTemp.value = (parseFloat(inTemp.value) - 32) * 5 / 9;
        }
        else if(inUnit.value === 'c' && outUnit.value === 'k') { // c->k
            outTemp.value = parseFloat(inTemp.value) + 273.15;
        }
        else if(inUnit.value === 'k' && outUnit.value === 'c') { // k->c
            outTemp.value = parseFloat(inTemp.value) - 273.15;
        }
        else if(inUnit.value === 'f' && outUnit.value === 'k') { // f->k
            outTemp.value = (parseFloat(inTemp.value) - 32) * 5 / 9 + 273.15;
        }
        else if(inUnit.value === 'k' && outUnit.value === 'f') { // k->f
            outTemp.value = (parseFloat(inTemp.value) - 273.15) * 9 / 5 + 32;
        }
    }
});