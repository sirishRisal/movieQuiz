$(document).ready(function () {

    var privilege_add_form=  $('#privilege_add_form')
    var privilege_edit_form = $('#privilege_edit_form')
    var edit_privilege_modal = $('#edit_privilege_modal')
    var add_privilege_modal = $('#add_privilege_modal')
    var privilege_add_btn = $('#privilege_add_btn')

    


    //adds new privileges
    privilege_add_form.submit(function (e) { 

        e.preventDefault();
        addPrivilege()
        //refreshing table if it's privilege Page
        if(window.location.pathname=='/admin/privileges'){
            add_privilege_modal.modal('hide')
            refreshPrivilegeTable()

        }
        
        
     })


     //functions for /admin/privileges page
     if(window.location.pathname=="/admin/privileges"){

        var privilege_dtable = $('#privilege_dtable').DataTable({destroy:true});
        refreshPrivilegeTable();

        privilege_add_btn.click(function(){
            //cleadring form fields
            $("input[name='name']").val('');
            $("input[name='description']").val('');

            add_privilege_modal.modal();

           
        });
        



     


  //selects edited row
  privilege_dtable.on( 'click', '.edit', function (e)
  {
        selected_tr = $(this).closest('tr');
        var data = privilege_dtable.row(selected_tr).data();

        $("input[name='name']").val(data.name);
        $("input[name='description']").val(data.description);

        edit_privilege_modal.modal('show');
    });

     //remove btn clicked
    privilege_dtable.on('click','.remove',function(e){
    // $tr = $(this).closest('tr');
    selected_tr = $(this).closest('tr');
    var data = privilege_dtable.row(selected_tr).data();
    del = confirm('Do you really want to delete '+data['name'] +' Privilege?')
    if(del){
        deletePrivilege(data)
    }

    

    });



    privilege_edit_form.submit(function (e) { 
        e.preventDefault();
        editPrivilege();
       
    });








    }
    function editPrivilege(){

        $.ajax({
            type: "POST",
            url: "api/privileges/edit",
            data: privilege_edit_form.serialize(),
            success: function (response) {

                if (response['status'] == 'SUCCESS'){

                    md.showNotification(response.status,'Sucessfully Updated');
                    refreshPrivilegeTable()
                    edit_privilege_modal.modal('hide')
                }else{
                    edit_privilege_modal.modal('hide')
                    md.showNotification(response.status,response.info.cause)
                }

                
            },
            error:function (error) { 
                edit_privilege_modal.modal('hide')
                md.showNotification('ERROR','Internal Server Error')
             }
        });
        
    }
    function deletePrivilege(data){

        $.ajax({

            'type':"POST",
            'url':'api/privileges/del',
             'data':data,
             success:function (response) {  

                if (response['status'] == 'SUCCESS'){

                    md.showNotification(response.status,'Sucessfully Deleted');
                    refreshPrivilegeTable()
                }else{
                    md.showNotification(response.status,response.info.cause)
                }
                

             },
             error:function (error) {  md.showNotification('ERROR','Internal server error') }
        });

    }

    function addPrivilege() { 
        $.ajax({
            type: "POST",
            url: "privilegeAdd",
            data: privilege_add_form.serialize(),
            success: function (response) {
                if (response['status'] == 'SUCCESS'){

                    md.showNotification(response.status,'Sucessfully Added');
                    privilege_add_form.trigger('reset');
                }else{
                    md.showNotification(response.status,response.info.cause)
                }
                

            },
            error:function (error) { md.showNotification('ERROR','Internal server error') }
        });
     }
     
    function populateTable(tableId,data){
        payload = []

        keys = Object.keys(data[0])

        $.each(keys,function (index,value) {  
            payload.push({'data':value})
        });
        var table = $('#'+tableId).DataTable({
                'data':data,
                columns:payload
        });

        return table

    }

    function refreshPrivilegeTable(){


        $.ajax({
            type:'POST',
            url:'api/privileges/list',
            success:function (response) {
                var actions = '<a href="#" class="edit"><i class="fa fa-edit"></i></a> <a href="#" class="remove"><i class="fa fa-times"></i></a>'
                $.each(response, function (index, value) { 
                    value['actions']=actions
                });

                privilege_dtable.clear().destroy()
                privilege_dtable = populateTable('privilege_dtable',response);
              },
            error:function (error) {  }

        });

    }






});