let game=true;
let turn=1;
let tag=document.createElement('p');
let textX=document.createTextNode('X');
let textO=document.createTextNode('O');

let box1=document.querySelector('#box-1');
let box2=document.querySelector('#box-2');
let box3=document.querySelector('#box-3');
let box4=document.querySelector('#box-4');
let box5=document.querySelector('#box-5');
let box6=document.querySelector('#box-6');
let box7=document.querySelector('#box-7');
let box8=document.querySelector('#box-8');
let box9=document.querySelector('#box-9');

if(game=true){

    box1.addEventListener('mouseover', (e)=>{
        Changebc(box1, turn);
    });
    box2.addEventListener('mouseover',(e)=>{
        Changebc(box2, turn);
    });
    box3.addEventListener('mouseover',(e)=>{
        e.preventDefault;
        Changebc(box3, turn);
    });
    box4.addEventListener('mouseover',(e)=>{
        Changebc(box4, turn);
    });
    box5.addEventListener('mouseover',(e)=>{
        Changebc(box5, turn);
    });
    box6.addEventListener('mouseover',(e)=>{
        Changebc(box6, turn);
    });
    box7.addEventListener('mouseover',(e)=>{
        Changebc(box7, turn);
    });
    box8.addEventListener('mouseover',(e)=>{
        Changebc(box8, turn);
    });
    box9.addEventListener('mouseover',(e)=>{
        Changebc(box9, turn);
    });
    
    function Changebc(box, turn){
        if(turn==1){
            tag.appendChild(textX);
            box.appendChild(tag);
            // box.style.background='green';
            // console.log(`Selected ${box}`);
        }
        else{
            tag.appendChild(textO);
            box.appendChild(tag);
        }
    }
    
    
    
}
