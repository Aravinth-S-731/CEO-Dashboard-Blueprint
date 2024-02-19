let navLinks = document.getElementById("navLinks");
let income_statement_table = document.getElementById("income-statement-table");

function openDashboardNav(){
    navLinks.style.left = "0";
}
function closeDashboardNav(){
    navLinks.style.left = "-200px";
}

const navListLinks = document.querySelectorAll('ul li');

console.log(role)
if  (role == "client" || role == "Employee" || role == "Manager") {
    alert("Apologies " + username + "! As a " + role + ", you are not authorized to access any of the features. Please ")
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
        if (text == 'Home' || text == 'Finance' || text == 'Chat' || text == 'Operational') {
            item.style.opacity = 0.5;
        }
    });
}

function createIncomeStatementTable() {
    const table = document.createElement('table');
    const tableData = income_data
    for (const rowData of tableData) {
        const row = document.createElement('tr');
        row.className = "table-row"
        for (const cellData of rowData) {
            const cell = document.createElement(rowData.indexOf(cellData) === 0 ? "th" : "td");
            cell.className = "table-cell"
            cell.textContent = cellData;
            row.appendChild(cell);
        }
        table.appendChild(row);
    }
    income_statement_table.appendChild(table);
}

createIncomeStatementTable();

// GROSS PROFIT MARGIN
var sum =0 , production_cost = 300, gross_profit_margin
for (let i = 0; i < revenue.length; i++) {
    sum += parseInt(revenue[i] / (30.5 * 12))
}
gross_profit_margin = Math.round(((sum - production_cost)/sum)*100)

// NET PROFIT MARGIN
var net_profit_margin, net_income_per_month = 0, revenue_per_month = 0
for (i = 0; i < revenue.length; i++) {
    net_income_per_month += (revenue[i] - expense[i])
    revenue_per_month += parseInt(revenue[i])
}
net_profit_margin = ((net_income_per_month/revenue_per_month)*100)

// OPEX RATION
var opex_ratio, revenue_ratio, profit_ratio, expense_per_month = 0
for (i=0; i < expense.length; i++) {
    expense_per_month += parseInt(expense[i])
}
opex_ratio = parseInt((expense_per_month/revenue_per_month)*100)
revenue_ratio = parseInt(revenue_per_month)/(30.5*12)
profit_ratio = parseInt((net_profit_margin+gross_profit_margin)/2)

// FORECASTING BUDGET
let total_revenue_2023 = 0, total_profit_2023 = 0, total_expense_2023 = 0
for (let i=0; i < revenue.length; i++) {
    total_revenue_2023 += parseInt(revenue[i])
    total_expense_2023 += parseInt(expense[i])
    total_profit_2023 += parseInt(profit[i])
}
let total_revenue_2024, total_expense_2024, total_profit_2024
total_revenue_2024 = parseInt(total_revenue_2023 + (total_revenue_2023/10))
total_expense_2024 = parseInt(total_expense_2023 + (total_expense_2023/10))
total_profit_2024 = parseInt(total_profit_2023 + (total_profit_2023/10))

// ----- DOUGHNUT CHART -----
const revenue_xValues = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"];

// Gross Profit Margin
new Chart ("gross-profit-chart", {
    type: 'doughnut',
    data: {
        labels: ['Gross Profit','Production Cost'],
        datasets: [{
            data: [gross_profit_margin, 100-gross_profit_margin],
            backgroundColor: ["#45ADFF","#45fff4"]
        }]
    },
    options: {
        rotation: -90,
        circumference: 180,
        maintainAspectRatio: true,
        aspectRatio: 1,
        responsive: false
    }
})

// OPEX ratio
new Chart ("opex-ratio-chart", {
    type: 'doughnut',
    data: {
        labels: ['OPEX Ratio','Profit'],
        datasets: [{
            data: [opex_ratio, profit_ratio],
            backgroundColor: ["#45ADFF","#45fff4"]
        }]
    },
    options: {
        rotation: -90,
        circumference: 180,
        maintainAspectRatio: true,
        aspectRatio: 1,
        responsive: false
    }
})

// Net Profit Margin
new Chart ("net-profit-chart", {
    type: 'doughnut',
    data: {
        labels: ['NET Profit','Expenditure'],
        datasets: [{
            data: [net_profit_margin, 100-net_profit_margin],
            backgroundColor: ["#45ADFF","#45fff4"]
        }]
    },
    options: {
        rotation: -90,
        circumference: 180,
        maintainAspectRatio: true,
        aspectRatio: 1,
        responsive: false
    }
})

// OPEX LINE CHART
new Chart("opex-line-chart", {
    type: "bar",
    data: {
        labels: revenue_xValues,
        datasets: [{
            label: "OPEX",
            data: expense,
            fill: false,
            borderColor: "rgba(69,173,255,1)",
            backgroundColor : "rgba(69,173,255,0.6)"
        },
        {
            label: "Profit",
            data: profit,
            fill: false,
            borderColor: "rgba(69,255,244,1)",
            backgroundColor : "rgba(69,255,244,0.6)"
        }]
    },
    options: {
        responsive: false,
        maintainAspectRatio: false,
    }
})

// FORECASTING LINE CHART
new Chart ("forecasting-line-chart", {
    type: 'pie',
    data: {
        labels: ["Revenue", "Expense", "Profit"],
        datasets: [
        {
            label: ["2024"],
            data: [total_revenue_2024, total_expense_2024, total_profit_2024],
            fill: true,
            backgroundColor: ["#45ADFF","#00cccc","#8289e8"]
        },
        {
            label: ["2023"],
            data: [total_revenue_2023, total_expense_2023, total_profit_2023],
            fill: true,
            backgroundColor: ["#45ADFF","#00cccc","#8289e8"]
        }
    ]
    },
    options: {
        responsive: false,
        maintainAspectRatio: false
    }
})