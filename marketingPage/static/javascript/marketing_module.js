let navLinks = document.getElementById("navLinks");
let sales_growth_percentage = document.getElementById('sales-growth-percentage')
let sales_target_percentage = document.getElementById('sales-target-percentage')

function openDashboardNav(){
    navLinks.style.left = "0";
}
function closeDashboardNav(){
    navLinks.style.left = "-200px";
}

const navListLinks = document.querySelectorAll('ul li');

console.log(role)
if  (role == "client" || role == "Employee") {
    alert("Apologies " + username + "! As a " + role + ", you are not authorized to access any of the features. Please ")
    openDashboardNav()
}
if (role == "Manager") {
    navListLinks.forEach(function(item) {
        const text = item.textContent.trim();
        if (text == 'Home' || text == 'Finance') {
            item.style.opacity = 0.5;
        }
    });
}
if (role == "Employee") {
    document.getElementById('marketing-module').style.display= 'none';
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
        if (text == 'Home' || text == 'Finance' || text == 'Chat' || text == 'Operational') {
            item.style.opacity = 0.5;
        }
    });
}

// Sales Growth Percentage Calculations
sales_growth_percentage.innerText = "Increase : " + Math.round(((profit[9] - profit[8]) / (revenue[9] - revenue[8])) * 100) + " %"


const revenue_xValues = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"];

// SALES GROWTH CHART
new Chart("sales-growth-chart", {
    type: 'bar',
    data: {
        labels: ['Revenue','Profit','Expense'],
        datasets: [{
            label: [revenue_xValues[8]],
            data: [revenue[8],profit[8],expense[8]],
            backgroundColor: ['#00cccc']
        },
        {
            label: [revenue_xValues[9]],
            data: [revenue[9],profit[9],expense[9]],
            backgroundColor: ['#45ADFF']
        }]
    },
    options: {
        responsive: false,
        maintainAspectRatio: false,
    }
})

// SALES TARGET CHART
let random_sales_count = parseInt(Math.random() * (800 - 700) + 700)
sales_target_percentage.innerText = "Achieved : " + Math.round((random_sales_count/1000) * 100) +" %"

new Chart("sales-target-chart", {
    type: 'doughnut',
    data: {
        labels: ['Sold', 'To be Sold'],
        datasets: [{
            label: [random_sales_count, 1000-random_sales_count],
            data: [random_sales_count, 1000-random_sales_count],
            backgroundColor: ["#45ADFF","#45fff4"]
        }]
    },
    options: {
        rotation: -90,
        circumference: 180,
        maintainAspectRatio: true,
        aspectRatio: 2,
        responsive: false
    }
})