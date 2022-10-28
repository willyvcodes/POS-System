import Swal from "sweetalert2";

export const show_toaster = (icon, message) => {
    const Toast = Swal.mixin({
        toast: true,
        position: 'top',
        showConfirmButton: false,
        timer: 2600,
        timerProgressBar: false,
        background: '#FFFFFF',
        color: '#2A3042',
    });

    Toast.fire({
        icon: icon,
        title: message
    });
}

export const show_confirm_dialog = (title, message, accept, cancel, callback, cancel_callback) => {
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
          confirmButton: 'btn btn-danger swal-btn-spacer',
          cancelButton: 'btn btn-light swal-btn-spacer',
        },
        buttonsStyling: false,
        focusConfirm: false,
        returnFocus: false,
    });
      
    swalWithBootstrapButtons.fire({
        title: title,
        text: message,
        padding: '1em',
        width: 400,
        returnFocus: false,
        reverseButtons: true,
        focusCancel: false,
        focusDeny: false,
        focusConfirm: true,
        allowEnterKey: true,
        confirmButtonText: accept,
        showCancelButton: true,
        cancelButtonText: cancel,

        background: '#FFFFFF',
        color: '#2A3042',
    }).then(result => {
        if (result.value) {
            callback();
        } else {
            if (cancel_callback != undefined) cancel_callback();
        }
    });
}