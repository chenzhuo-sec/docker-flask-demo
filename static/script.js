async function loadProducts() {
    const res = await fetch("/api/products");
    const products = await res.json();

    const container = document.getElementById("product-list");
    container.innerHTML = "";

    products.forEach((p) => {
        const card = document.createElement("div");
        card.className = "product-card";
        card.innerHTML = `
            <img src="${p.image}" alt="${p.name}">
            <h3>${p.name}</h3>
            <p>价格: ¥${p.price}</p>
        `;
        container.appendChild(card);
    });
}

// 初始化加载
loadProducts();

// 刷新按钮
document.getElementById("refreshBtn").addEventListener("click", loadProducts);
