  var data = {
          resource_id: '079fd017-dfa3-4e69-9198-72fcb4b2f01c', // the resource id
          limit: 5, // get 5 results
          q: 'jones' // query for 'jones'
        };
        $.ajax({
          url: 'http://dados.recife.pe.gov.br/pt_BR/api/3/action/datastore_search',
          data: data,
          dataType: 'jsonp',
          success: function(data) {
            alert('Total results found: ' + data.result.total)
          }
        });
   
