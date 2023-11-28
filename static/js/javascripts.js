// let btn_minus = document.getElementById('btn_minus')

// btn_minus.addEventListener('click',() => {
//     let  qlt_input = document.getElementById('qlt')
//     qlt = qlt_input.value
//     if
//     ( qlt >= 2){
//         qlt--
//     }
//     qlt_input.value = qlt
// })

// let btn_plus = document.getElementById('btn_plus')

// btn_plus.addEventListener('click',()=>{
//     let  qlt_input =document.getElementById('qlt')
//     qlt =qlt_input.value

//     qlt++

//     qlt_input.value =qlt
// })

function increment(e){
    let qty_id = e.target.getAttribute('data-qtyId');
    let qty_input = document.getElementById(qty_id)
    qty_input.value = parseInt(qty_input.value) + 1;
}

function decrement(e){
    
        let qty_id = e.target.getAttribute('data-qtyId');
        let qty_input = document.getElementById(qty_id)
        const value = qty_input.value;
        if(value >1){
        qty_input.value = parseInt(value) - 1;
    }
}
