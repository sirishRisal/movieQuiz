
  $.ajax({
      url: '/index',
      // data: JSON.stringify(data),
      type: 'POST',
      contentType: 'application/json;',
       success: function(response) {
       	alert(JSON.stringify(response))
        
                          
      },            
      error: function(error) {
          alert(error);
      }
    });
       
