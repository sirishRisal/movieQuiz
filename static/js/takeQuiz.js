
$.ajax({
  url: '/getQuizQuestion',
  // data: JSON.stringify(values),
  type: 'GET',
  contentType: 'application/json;',
   success: function(response) {
    // var x=JSON.parse(response)
    //   alert(x[0]["id"])
          addQuestion(JSON.parse(response))
  },            
  error: function(error) {
      alert(error);
  }
});





function makeOptions(data,id){
  // alert(data)
  var htmlOption='<div class="form-check">\
          <label class="form-check-label">\
              '+data+'\
              <input class="form-check-input" required="" name="'+id+'" type="checkbox" value="'+data+'">\
              <span class="form-check-sign">\
              <span class="check"></span>\
              </span>\
          </label>\
      </div>';
      return(htmlOption)
}

function makeQuestion(data){

  
  var html=""
  html+='<div>'
  html+='<h3>'+data["question"]+'?</h3>';
  html+='<div class="questionOptions">';
        for(j in data["options"]){
          // alert(JSON.stringify(data["options"][j]+" skdjnaks"))
          html+=makeOptions(data["options"][j],data["id"])
        }
        html+='</div></form><hr>';
        return(html)
  // alert(html)

}

function addQuestion(x){
  // alert(x)
  var htmlInsert='<form method="post">';    
  for(i in x){
    // alert(JSON.stringify(x[i]["id"]))

  htmlInsert+=makeQuestion(x[i]);
  }
   htmlInsert+='<button type="submit" class="btn btn-primary pull-right">Submit</button></form>';
  $("#quizQuestions").html(htmlInsert);

  
$("input:checkbox").on('click', function() {
  // in the handler, 'this' refers to the box clicked on
  var $box = $(this);
  if ($box.is(":checked")) {
    // the name of the box is retrieved using the .attr() method
    // as it is assumed and expected to be immutable
    var group = "input:checkbox[name='" + $box.attr("name") + "']";
    // the checked state of the group/box on the other hand will change
    // and the current value is retrieved using .prop() method
    $(group).prop("checked", false);
    $box.prop("checked", true);
    $(group).prop("required", false);
  } else {
    $box.prop("checked", false);
    $box.prop("required", true);
  }
});


 $('form').submit(function (e) { 
        e.preventDefault();
        
        var values = [];
        $('input[type="checkbox"]:checked').each(function(i,v){
          
          var ans={"questionId":v.name,"answer":$(v).val()}
          values.push(ans);
        });
        
        
              $.ajax({
                  url: '/quiz',
                  data: JSON.stringify(values),
                  type: 'POST',
                  contentType: 'application/json;',
                   success: function(response) {
                    if(response["status"]=="ok")
                    md.showNotification('SUCCESS',"Submitted successfully")
                      window.location = 'http://127.0.0.1:5000/index';
                                      
                  },            
                  error: function(error) {
                      alert(error);
                  }
                });
       
    });


}




