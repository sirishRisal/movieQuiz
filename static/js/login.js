// $('form').submit(function (e) { 
//     e.preventDefault();
//     var username=$("#username").val();
//     var password=$("#password").val();
//     data={"username":username,"password":password}
        
//         // alert(JSON.stringify(data))
        
//               $.ajax({
//                   url: '/',
//                   data: JSON.stringify(data),
//                   type: 'POST',
//                   contentType: 'application/json;',
//                    success: function(response) {
//                     if(response!="already"){
//                       html="<a href="+response+">click here to activate account</a>"
//                       $("#linkToActivate").html(html)
//                     }
//                     else{
//                       alert("try with different username or email")
//                     }
                                      
//                   },            
//                   error: function(error) {
//                       alert(error);
//                   }
//                 });
       
//     });