$(function() {

  var loadForm = function() {
    var btn = $(this);
    $.ajax({
      url: btn.attr('data-url'),
      type: 'GET',
      dataType: 'json',
      beforeSend: function() {
        $('#modal-status').modal('show');
      },
      success: function(data) {
        $('#modal-status .modal-content').html(data.html_form);
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
          $('#modal-status').modal('hide');
          $('#status-table tbody ').html(data.html_status_list);
          $('#detail-status').html(data.html_status_detail);
        } else {
          $('#modal-status .modal-content').html(data.html_form);
        }

      }
    });
    return false;
  };

  //  create company
  $('.js-create-status').click(loadForm);
  $('#modal-status').on('submit', '.js-status-create-form', saveForm);

  //  update company
  $('#edit-status').click(loadForm);
  $('#modal-status').on('submit', '.js-status-update-form', saveForm);
});