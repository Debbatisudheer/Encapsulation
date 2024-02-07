let balance = 1000; // Initial balance
const accountNumber = 1234567890;

function deposit() {
    const amount = parseInt(document.getElementById('amount').value);
    if (amount > 0) {
        balance += amount;
        updateAccountDetails();
    } else {
        alert('Please enter a valid amount.');
    }
}

function withdraw() {
    const amount = parseInt(document.getElementById('amount').value);
    if (amount > 0 && amount <= balance) {
        balance -= amount;
        updateAccountDetails();
    } else {
        alert('Insufficient funds or invalid amount.');
    }
}

function updateAccountDetails() {
    document.getElementById('account-details').innerHTML = `Account Number: ${accountNumber}<br>Balance: $${balance}`;
}