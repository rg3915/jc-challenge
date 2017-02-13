$(function() {

  var loadForm = function() {
    var btn = $(this);
    $.ajax({
      url: btn.attr('data-url'),
      type: 'GET',
      dataType: 'json',
      beforeSend: function() {
        $('#modal-company').modal('show');
      },
      success: function(data) {
        $('#modal-company .modal-content').html(data.html_form);
      }
    });
  };

  var saveForm = function() {
    var form = $(this);

    $.ajax({
      url: form.attr('action'),
      type: form.attr('method'),
      data: form.serialize(),
      dataType: 'json',
      success: function(data) {
        if (data.is_form_valid) {
          $('#modal-company').modal('hide');
          $('#company-table tbody ').html(data.html_company_list);
          $('#detail-company ').html(data.html_company_detail);
        } else {
          $('#modal-company .modal-content').html(data.html_form);
        }

      }
    });
    return false;
  };

  //  create company
  $('.js-create-company').click(loadForm);
  $('#modal-company').on('submit', '.js-company-create-form', saveForm);

  //  update company
  $('#edit-company').click(loadForm);
  $('#modal-company').on('submit', '.js-company-update-form', saveForm);

  //  delete company
  // $('#company-table').on('click', '.js-company-delete', loadForm);
  // $('#modal-company').on('submit', '.js-company-delete-form', saveForm)
});