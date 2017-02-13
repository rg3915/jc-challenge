$(function() {

  var loadForm = function() {
    var btn = $(this);
    $.ajax({
      url: btn.attr('data-url'),
      type: 'GET',
      dataType: 'json',
      beforeSend: function() {
        $('#modal-person').modal('show');
      },
      success: function(data) {
        $('#modal-person .modal-content').html(data.html_form);
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
          $('#person-table tbody').html(data.html_person_list);
          $('#modal-person').modal('hide');
        } else {
          $('#modal-person .modal-content').html(data.html_form);
        }

      }
    });
    return false;
  };

  //  create person
  $('.js-create-person').click(loadForm);
  $('#modal-person').on('submit', '.js-person-create-form', saveForm);

  //  update person
  $('#edit-person').click(loadForm);
  $('#modal-person').on('submit', '.js-person-update-form', saveForm);

});