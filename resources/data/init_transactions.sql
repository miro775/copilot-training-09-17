INSERT INTO transaction (account_id, klient_id, type, amount, timestamp, description) VALUES
(1, 1, 'deposit', 1000, CURRENT_TIMESTAMP, 'Initial deposit'),
(2, 2, 'deposit', 1000, CURRENT_TIMESTAMP, 'Initial deposit'),
(1, 1, 'withdraw', 200, CURRENT_TIMESTAMP, 'ATM withdrawal'),
(2, 2, 'transfer_in', 200, CURRENT_TIMESTAMP, 'Transfer from account 1');
