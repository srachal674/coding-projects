fetch("projects.json")
    .then(response => response.json())
    .then(data => {

        const modalTitle = document.getElementById("projectModalTitle");
        const modalBody = document.getElementById("projectModalBody");

        const copyButton = document.getElementById("copyProject");
        const pdfButton = document.getElementById("savePdf");

        const allProjects = [
            ...data.codingProjects,
            ...data.businessMarketingEntrepreneurship,
            ...data.graphicDesign
        ];

        const buttons = document.querySelectorAll(".project-button");

        buttons.forEach(button => {
            button.addEventListener("click", () => {

                const projectName = button.dataset.project;

                const project = allProjects.find(
                    item => item.name === projectName
                );

                modalTitle.textContent = project.name;

                modalBody.innerHTML = project.description;

                const modal = new bootstrap.Modal(
                    document.getElementById("projectModal")
                );

                modal.show();
            });
        });        
    });