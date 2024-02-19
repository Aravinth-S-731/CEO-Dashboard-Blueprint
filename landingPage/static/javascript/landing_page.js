let navLinks = document.getElementById("navLinks");
const transactionHistoryDiv = document.getElementById("transaction-history");

function openDashboardNav(){
    navLinks.style.left = "0";
}
function closeDashboardNav(){
    navLinks.style.left = "-200px";
}

const navListLinks = document.querySelectorAll('ul li');

console.log(role)
if  (role == "Employee" || role == "Manager" || role == "Client") {
    document.getElementById('dashboard-home').style.display = 'none';
    alert("Apologies " + username + "! As a " + role + ", you are not authorized to access any of the features.")
    openDashboardNav()
    navListLinks.forEach(function(item) {
        const text = item.textContent.trim();
        if (text == 'Home' || text == 'Finance') {
            item.style.opacity = 0.5;
        }
    });
}
if (role == "Employee") {
    navListLinks.forEach(function(item) {
        const text = item.textContent.trim();
        if (text == 'Home' || text == 'Finance' || text == 'Marketing') {
            item.style.opacity = 0.5;
        }
    });
}
if (role == "Client") {
    navListLinks.forEach(function(item) {
        const text = item.textContent.trim();
        if (text == 'Home' || text == 'Finance' || text == 'Operational' || text == 'Chat' ) {
            item.style.opacity = 0.5;
        }
    });
}



function createTransactionHistory() {
    const transactions = [
        { name: "Aravinth", type: "Debited", amount: "- ₹ 36,577", imgSrc: "https://i.pravatar.cc/40?img=68" },
        { name: "Mohammed Sherif", type: "Credited", amount: "+ ₹ 16,760", imgSrc: "https://i.pravatar.cc/40?img=67" },
        { name: "Sree Valsan", type: "Credited", amount: "+ ₹ 6,700", imgSrc: "https://i.pravatar.cc/40?img=66" },
        { name: "Raghavan", type: "Debited", amount: "- ₹ 32,775", imgSrc: "https://i.pravatar.cc/40?img=65" },
        { name: "Aravind", type: "Credited", amount: "+ ₹ 12,500", imgSrc: "https://i.pravatar.cc/40?img=61" },
    ];
    document.getElementById('balance-amount').innerText = '₹ 36,06,747';
    document.getElementById('account-number').innerText = '1561 00** **** 250';
    function createTransactionHTML(transaction, index) {
        return `
            <div class="person-${index + 1} person">
            <div class="transaction-info">
                <img src="${transaction.imgSrc}" alt="Avatar">
                <div class="transaction-detail">
                <h4 class="person-name">${transaction.name}</h4>
                <h6 class="transaction-type ${transaction.type.toLowerCase()}">${transaction.type}</h6>
                </div>
            </div>
            <div class="transaction-amount ${transaction.type.toLowerCase()}">
                <h4 class="${transaction.type.toLowerCase()}">${transaction.amount}</h4>
            </div>
            </div>
        `;
    }
    transactions.forEach((transaction, index) => {
        transactionHistoryDiv.innerHTML += createTransactionHTML(transaction, index);
    });
}

createTransactionHistory();


const totalDuration = 5000;
const delayBetweenPoints = totalDuration / 12;
const previousY = (ctx) => ctx.index === 0 ? ctx.chart.scales.y.getPixelForValue(100) : ctx.chart.getDatasetMeta(ctx.datasetIndex).data[ctx.index - 1].getProps(['y'], true).y;
const animation = {
    x: {
        type: 'number',
        easing: 'linear',
        duration: delayBetweenPoints,
        from: NaN, // the point is initially skipped
        delay(ctx) {
        if (ctx.type !== 'data' || ctx.xStarted) {
            return 0;
        }
        ctx.xStarted = true;
        return ctx.index * delayBetweenPoints;
        }
    },
    y: {
        type: 'number',
        easing: 'linear',
        duration: delayBetweenPoints,
        from: previousY,
        delay(ctx) {
        if (ctx.type !== 'data' || ctx.yStarted) {
            return 0;
        }
        ctx.yStarted = true;
        return ctx.index * delayBetweenPoints;
        }
    }
};

const revenue_xValues = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"];

new Chart("revenue-line-chart", {
    type: "line",
    data: {
        labels: revenue_xValues,
        datasets: [{
            label: "Revenue Generated",
            fill: true,
            hoverBackgroundColor: "#555",
            lineTension: 0,
            backgroundColor: "#8289e850",
            borderColor: "#45ADFF",
            data: revenue,
        }]
        },
        options: {
            animation,
            maintainAspectRatio: true,
            aspectRatio: 3,
            responsive: true,
            legend: {display: true},
            scales: {
            yAxes: [{ticks: {min: 6, max:16}}],
            }
    }
});

new Chart("payment-pie-chart", {
    type: 'pie',
        data: {
            labels: ["Credit", "Debit", "UPI"],
            datasets: [{
                data: payment_mode,
                backgroundColor: ['#45ADFF', '#00cccc', '#8289e8'],
                hoverOffset: 5
            }],
        },
        options: {
            maintainAspectRatio: true,
            aspectRatio: 2.5,
            responsive: true,
        },
})

new Chart("profit-bar-chart", {
    type: 'bar',
    data: {
        labels: revenue_xValues,
        datasets: [{
            label: "profit",
            data: profit,
        }]
    },
    options: {
        maintainAspectRatio: true,
        aspectRatio: 2,
        responsive: true
    }
})