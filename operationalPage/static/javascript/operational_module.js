let navLinks = document.getElementById("navLinks");

function openDashboardNav(){
    navLinks.style.left = "0";
}
function closeDashboardNav(){
    navLinks.style.left = "-200px";
}

const navListLinks = document.querySelectorAll('ul li');

console.log(role)
if  (role == "client") {
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
    navListLinks.forEach(function(item) {
        const text = item.textContent.trim();
        if (text == 'Home' || text == 'Finance' || text == 'Marketing') {
            item.style.opacity = 0.5;
        }
    });
}
if (role == "Client") {
    document.getElementById('operational-module').style.display= 'none';
    navListLinks.forEach(function(item) {
        const text = item.textContent.trim();
        if (text == 'Home' || text == 'Finance' || text == 'Chat' || text == 'Operational') {
            item.style.opacity = 0.5;
        }
    });
}


// Employee Per Department
new Chart("emp-per-dept", {
    type: 'bar',
    data: {
        labels: Object.keys(employee_count_per_department),
        datasets: [{
            label: "Employee per Department",
            data: [employee_count_per_department['HR'],
                    employee_count_per_department['IT'],
                    employee_count_per_department['accounts'],
                    employee_count_per_department['creative team'],
                    employee_count_per_department['management'],
                    employee_count_per_department['media'],
                    employee_count_per_department['research']],
            backgroundColor: ['rgba(69, 173, 255, 0.5)'],
            borderColor: ["#45adff"]
        }]
    },
    options: {
        indexAxis: 'y',
        responsive: false,
        // maintainAspectRatio: true,
        // aspectRatio: 2,
        scales: {
            x: {
                grid: {
                    display: false
                }
            },
            y: {
                grid: {
                    display: false
                }
            }
        }
    }
})

// Average Salary By Department
new Chart("avg-salary-by-dept", {
    type: 'bar',
    data: {
        labels: Object.keys(average_salary_per_department),
        datasets: [{
            label: "Average Salary by Departments",
            data: [average_salary_per_department['HR'],
                    average_salary_per_department['IT'],
                    average_salary_per_department['accounts'],
                    average_salary_per_department['creative team'],
                    average_salary_per_department['management'],
                    average_salary_per_department['media'],
                    average_salary_per_department['research']],
            backgroundColor: ["#45adff"]
        }]
    },
    options: {
        responsive: false,
        // maintainAspectRatio: true,
        // aspectRatio: 3
    }
})

// Salary range Breakdown Values
let salary_range_breakdown = []
for (let i = 0; i < Object.keys(salary_range_of_employee).length; i++) {
    salary_range_breakdown.push(salary_range_of_employee[Object.keys(salary_range_of_employee)[i]])
}
// Salary Range Breakdown
new Chart("salary-range-breakdown-amt", {
    type: 'line',
    data: {
        labels: Object.keys(salary_range_of_employee),
        datasets: [{
            label: "Salary Range Breakdown",
            data: salary_range_breakdown,
            fill: true,
            backgroundColor: "rgba(69, 173, 255, 0.3)",
            borderColor: "#45adff"
        }]
    }
})

// Contribution per Department
let total_contribution = 0;
const contribution_per_department = [];
const contribution_per_department_percentage = [];
Object.entries(average_salary_per_department).forEach(([key, value], i) => {
    const contribution = Math.round(value / employee_count_per_department[key]);
    contribution_per_department.push(contribution);
    total_contribution += contribution;
});
contribution_per_department.forEach((contribution) => {
    contribution_per_department_percentage.push(Math.round((contribution / total_contribution) * 100));
});
// Contribution Chart
new Chart("contribution-chart", {
    type: 'doughnut',
    data: {
        labels: Object.keys(employee_count_per_department),
        datasets: [{
            label: "Contributes",
            data: contribution_per_department_percentage
        }]
    },
    options: {
        maintainAspectRatio: true,
        responsive: false,
        plugins: {
            legend: {
                display: true,
                position: 'left',
                maxHeight: 50,
                maxWidth: 150,
                fullSize: true,
            }
        }
    }
})

// Gender Chart
new Chart('gender-chart', {
    type: 'doughnut',
    data: {
        labels: ["Male","Female"],
        datasets: [{
            data: [employees_gender_count['male'], employees_gender_count['female']],
            backgroundColor: ["#45baff","#FF5177"]
        }]
    }
})