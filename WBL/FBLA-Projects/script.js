fetch("projects.json")
    .then(response => response.json())
    .then(data => {

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

                document.getElementById("projectModalTitle").textContent =
                    project.name;

                document.getElementById("projectModalBody").textContent =
                    project.description;

                const modal = new bootstrap.Modal(
                    document.getElementById("projectModal")
                );

                modal.show();
            });
        });
    });