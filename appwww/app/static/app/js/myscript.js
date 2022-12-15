$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 2,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 4,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 6,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('.plus-basket').click(function(){
    // console.log("clickplus")
    // console.log(this.parentNode.children[2])
    var id = $(this).attr("pid").toString();
    // console.log("produktId: ",prodid)
    var il = this.parentNode.children[2]
    // console.log("ilość: ", this.parentNode.children[2])
    $.ajax({
        type:"GET",
        url:"/plusbasket",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log("data: ", data)
            il.innerText=data.amount
            //amount=cena
            //quantity=ilosc
            // totalcost = cenacalkowita
            document.getElementById("ile").innerText=data.ile 
            document.getElementById("totalcost").innerText=data.totalcost
        }
    })
})

$('.minus-basket').click(function(){
    var id=$(this).attr("pid").toString();
    var il=this.parentNode.children[2] 
    $.ajax({
        type:"GET",
        url:"/minusbasket",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log("data: ", data)
            il.innerText=data.amount 
            document.getElementById("ile").innerText=data.ile 
            document.getElementById("totalcost").innerText=data.totalcost
        }
    })
})


$('.remove-basket').click(function(){
    var id=$(this).attr("pid").toString();
    console.log("click")
    console.log(id)
    var il=this
    $.ajax({
        type:"GET",
        url:"/removebasket",
        data:{
            prod_id:id
        },
        success:function(data){
            document.getElementById("ile").innerText=data.ile 
            document.getElementById("totalcost").innerText=data.totalcost
            il.parentNode.parentNode.parentNode.parentNode.remove()  //usun caly div
        }
    })
})


// $('.plus-wishlist').click(function(){
//     var id=$(this).attr("pid").toString();
//     $.ajax({
//         type:"GET",
//         url:"/pluswishlist",
//         data:{
//             prod_id:id
//         },
//         success:function(data){
//             //alert(data.message)
//             window.location.href = `http://localhost:8000/product-detail/${id}`
//         }
//     })
// })


// $('.minus-wishlist').click(function(){
//     var id=$(this).attr("pid").toString();
//     $.ajax({
//         type:"GET",
//         url:"/minuswishlist",
//         data:{
//             prod_id:id
//         },
//         success:function(data){
//             window.location.href = `http://localhost:8000/product-detail/${id}`
//         }
//     })
// })