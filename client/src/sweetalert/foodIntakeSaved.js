import Swal from "sweetalert2";

export function FoodIntakeSaved() {
  Swal.fire({
    title: "Food Intake Saved Successfully!",
    icon: "success",
    showCancelButton: true,
    confirmButtonColor: "#5b5b5b",
    cancelButtonColor: "rgb(22, 109, 16)",
    reverseButtons: true,
    confirmButtonText: "Add another intake",
    cancelButtonText: `<a href="/">${"Go to home page"}</a>`,

    preConfirm: () => {
      window.location.href = "/";
    },
    preDeny: () => {},
  });
}

export default FoodIntakeSaved;
