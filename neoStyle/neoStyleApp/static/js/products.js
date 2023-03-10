//BRAND

const brandCheckboxes = document.querySelectorAll('.brand-checkbx');

brandCheckboxes.forEach(function(checkbox) {
  checkbox.addEventListener('change', function() {
    // Get the ID of the selected brand
    const selectedBrandId = this.value;

    // If the checkbox is checked and a brand is selected
    if (this.checked && selectedBrandId) {
      // Redirect to the appropriate URL with the selected brand ID
      window.location.href = `/products/?brands=${selectedBrandId}`;
    }
  });
});


//GENDER
const genderCheckboxes = document.querySelectorAll('.gender-checkbx');

genderCheckboxes.forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {
      
      const selectedGenderId = this.value;
  
      if (this.checked && selectedGenderId) {
    
        window.location.href = `/products/?genders=${selectedGenderId}`;
      }
    });
});
  
// SHOW/HIDE FILTERS 

let filterSection = document.querySelector('.categories-section');
let filtersBtn = document.querySelector('.filters-btn');
let closeBtn = document.querySelector('.close-btn');

filtersBtn.addEventListener ('click', () => {

    filterSection.classList.add('activate')

})

closeBtn.addEventListener("click", () => {

  filterSection.classList.remove('activate')
})


