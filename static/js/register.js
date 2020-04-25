$('form').submit(function (e) { 
    e.preventDefault();
    var email=$("#email").val();
    var username=$("#username").val();
    var password=$("#password").val();
    data={"email":email,"username":username,"password":password}
        
              $.ajax({
                  url: '/register',
                  data: JSON.stringify(data),
                  type: 'POST',
                  contentType: 'application/json;',
                   success: function(response) {

                    if(response!="already"){



                      html="<div class=\"alert alert-success col-sm-3\"><a href="+response+">Successfully registered click here to activate account</a></div>";
                      $("#res").html(html)
                    }
                    else{
                      html="<div class=\"alert alert-success col-sm-3\">try with different username or email</div>";
                      $("#res").html(html)
                      
                    }
                                      
                  },            
                  error: function(error) {
                      alert(error);
                  }
                });
       
    });