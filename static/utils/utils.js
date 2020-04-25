function request(url,data,method,callback,md){
    $.ajax({
        type: method,
        url: url,
        data: data,
        success: function (response) {
            callback(response);
        },
        error:function (error) {md.showNotification('ERROR','Internal server error')}
    });
}
function showNotification(response,msg,md) { 
    if (response.status=='SUCCESS'){

        md.showNotification(response.status,msg)
        return true

    }else if (response.status=='ERROR'){

        md.showNotification(response.status,response.info.cause)
        return false
    }
 }

 function populateTable(tableId,data){
    var payload = []

    var keys = Object.keys(data[0])

    $.each(keys,function (index,value) {  
        payload.push({'data':value})
    });
    var table = $('#'+tableId).DataTable({
            'data':data,
            columns:payload
    });

    return table

}

export {request,showNotification,populateTable}