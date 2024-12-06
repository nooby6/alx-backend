import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();
const app = express();
const port = 1245;

/**
 * List of products available in stock.
 * @typedef {Object} Product
 * @property {number} itemId - The unique identifier for the product.
 * @property {string} itemName - The name of the product.
 * @property {number} price - The price of the product.
 * @property {number} initialAvailableQuantity - The initial quantity of the product available in stock.
 */

/**
 * An array of products.
 * @type {Product[]}
 */
const listProducts = [{
  itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4,
}, {
  itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10,
}, {
  itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2,
}, {
  itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5,
}];

function getItemById(id) {
  return listProducts.find(({ itemId }) => itemId === id);
}

function reserveStockById(itemId) {
  client.incr(`item.${itemId}`);
}

const getAsync = promisify(client.get).bind(client);
async function getCurrentReservedStockById(itemId) {
  const reservedStock = await getAsync(`item.${itemId}`);
  return reservedStock;
}

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});

app.get('/list_products', (req, resp) => {
  resp.json(listProducts);
});

app.get('/list_products/:itemId', async (req, resp) => {
  const id = Number(req.params.itemId);
  const product = getItemById(id);
  if (!product) {
    resp.json({ status: 'Product not found' });
  }
  const reservedStock = await getCurrentReservedStockById(id);
  product.currentQuantity = product.initialAvailableQuantity - reservedStock;
  resp.json(product);
});

app.get('/reserve_product/:itemId', async (req, resp) => {
  const id = Number(req.params.itemId);
  const product = getItemById(id);
  if (!product) {
    resp.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(id);
  if ((product.initialAvailableQuantity - reservedStock) < 1) {
    resp.json({ status: 'Not enough stock available', itemId: product.itemId });
  }
  reserveStockById(product.itemId);
  resp.json({ status: 'Reservation confirmed', itemId: product.itemId });
});