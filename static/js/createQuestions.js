$(document).ready(function(){
    var maxField = 10; //Input fields increment limitation
    var addButton = $('.add_button'); //Add button selector
    var wrapper = $('.field_wrapper'); //Input field wrapper
    var fieldHTML = '<div><input required="" type="text" name="field_name[]" value=""/><a href="javascript:void(0);" class="remove_button"><img src="http://demos.codexworld.com/add-remove-input-fields-dynamically-using-jquery/images/remove-icon.png"/></a></div>'; //New input field html 
    var x = 1; //Initial field counter is 1
    
    //Once add button is clicked
    $(addButton).click(function(){
        //Check maximum number of input fields
        if(x < maxField){ 
            x++; //Increment field counter
            $(wrapper).append(fieldHTML); //Add field html
        }
    });
    
    //Once remove button is clicked
    $(wrapper).on('click', '.remove_button', function(e){
        e.preventDefault();
        $(this).parent('div').remove(); //Remove field html
        x--; //Decrement field counter
    });
});
   


   $('#question_form').submit(function (e) { 
        e.preventDefault();
        var answer=$("input[name=correctAnswer]").val().toLowerCase().trim();
        var values = [];
        $("input[name='field_name[]']").each(function() {
            values.push($(this).val().toLowerCase().trim());
        });
        if (values.length<2) {
          md.showNotification('ERROR',"Option must be more than two")

        }else{
          var includeAnswer = values.includes(answer);
          if(includeAnswer){
             data={"question":$("input[name=question]").val(),"answer":answer,"options":values }
              // alert(JSON.stringify(data))
              $.ajax({
                  url: '/createquestions',
                  data: JSON.stringify(data),
                  type: 'POST',
                  contentType: 'application/json;',
                   success: function(response) {
                    md.showNotification('SUCCESS',response)
                    window.location = 'http://127.0.0.1:5000/createquestions';
                      
                                      
                  },            
                  error: function(error) {
                      alert(error);
                  }
                });
          }
          else{
            md.showNotification('ERROR',"no answer in options")
          }
        }
       
    });






// function editdocument(){
//         $.ajax({
//             type: "POST",
//             url: "api/document/edit",
//             data: user_document_edit_form.serialize()+'&id='+id,
//             success: function (response) {
//                 if (response['status'] == 'SUCCESS'){
//                     md.showNotification(response.status,'Sucessfully Updated');
//                     edit_document_modal.modal('hide');
//                     refreshuserdocumentTable()

//                 }else{
//                     edit_document_modal.modal('hide');
//                     md.showNotification(response.status,response.info.cause)
//                 }

                
//             },
//             error:function (error) { 
//                 edit_document_modal.modal('hide')
//                 md.showNotification('ERROR','Internal Server Error')
//              }
//         });
        
//     }
