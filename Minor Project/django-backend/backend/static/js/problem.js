document.addEventListener("DOMContentLoaded", function () {
    const resultDiv = document.getElementById('result');
    const submitBtn = document.getElementById('submitBtn');
    const form = document.getElementById('codeForm');

    // Move the onmessage event listener outside of the submitBtn click event
    window.onmessage = function (e) {
        // Handle the e.data which contains the code object
        const code = e.data.files[0].content;
        const lang = e.data.language;
        // Update the hidden form field when the Submit button is clicked
        document.getElementById('codeInput').value = code;
        document.getElementById('languageInput').value = 'python3';
    };

    submitBtn.addEventListener('click', function (e) {
        e.preventDefault();
        submitBtn.disabled = true;
        resultDiv.innerText = 'Testcases Executing...';

        fetch('', {
            method: 'POST',
            body: new FormData(form)
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerText = `
                Tests Passed: ${data.TestcasesPassed}
                Tests Failed: ${data.TestcasesFailed}`;
            submitBtn.disabled = false;
        })
        .catch(error => {
            resultDiv.innerText = 'Error submitting tests';
            submitBtn.disabled = false;
        });
    });
});
