const colorButtons = document.querySelectorAll('.box');
const reset = document.querySelector('.reset');
const body = document.querySelector('body');

colorButtons.forEach(function(button){
    console.log(button);
    button.addEventListener('click', function(e){
        if(e.target.id === 'red'){
            body.style.backgroundColor = e.target.id;
        }
        else if(e.target.id === 'green'){
            body.style.backgroundColor = e.target.id;
        }
        else if(e.target.id === 'blue'){
            body.style.backgroundColor = e.target.id;
        }
        else if(e.target.id === 'yellow'){
            body.style.backgroundColor = e.target.id;
        }
    })
})

reset.addEventListener('click', function(){
    body.style.backgroundColor = '#1f1f1f';
})