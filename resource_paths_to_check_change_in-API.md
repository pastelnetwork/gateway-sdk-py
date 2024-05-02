### Login
pastel_gateway_sdk/api/login_api.py:387:            resource_path='/api/v1/login/access-token',
pastel_gateway_sdk/api/login_api.py:1163:           resource_path='/api/v1/login/test-token',
pastel_gateway_sdk/api/login_api.py:647:            resource_path='/api/v1/password-recovery/{email}',
pastel_gateway_sdk/api/login_api.py:920:            resource_path='/api/v1/reset-password/',

### Users
pastel_gateway_sdk/api/users_api.py:312:            resource_path='/api/v1/users',
pastel_gateway_sdk/api/users_api.py:1630:           resource_path='/api/v1/users',
pastel_gateway_sdk/api/users_api.py:846:            resource_path='/api/v1/users/{user_id}',
pastel_gateway_sdk/api/users_api.py:1107:           resource_path='/api/v1/users/{user_id}',
pastel_gateway_sdk/api/users_api.py:1919:           resource_path='/api/v1/users/{user_id}',
pastel_gateway_sdk/api/users_api.py:1350:           resource_path='/api/v1/users/me',
pastel_gateway_sdk/api/users_api.py:2193:           resource_path='/api/v1/users/me',
pastel_gateway_sdk/api/users_api.py:585:            resource_path='/api/v1/users/open',

### Account
pastel_gateway_sdk/api/account_api.py:1329:         resource_path='/api/v1/account/total_balances',
pastel_gateway_sdk/api/account_api.py:275:          resource_path='/api/v1/account/my_total_balance',
pastel_gateway_sdk/api/account_api.py:1089:         resource_path='/api/v1/account/set_balance_limit',
pastel_gateway_sdk/api/account_api.py:535:          resource_path='/api/v1/account/pastelid_claiming_step_1',
pastel_gateway_sdk/api/account_api.py:812:          resource_path='/api/v1/account/pastelid_claiming_step_2',

### API Keys
pastel_gateway_sdk/api/api_keys_api.py:309:         resource_path='/api/v1/api_keys',
pastel_gateway_sdk/api/api_keys_api.py:1111:        resource_path='/api/v1/api_keys',
pastel_gateway_sdk/api/api_keys_api.py:570:         resource_path='/api/v1/api_keys/{api_key}',
pastel_gateway_sdk/api/api_keys_api.py:831:         resource_path='/api/v1/api_keys/{api_key}',

### Cascade
pastel_gateway_sdk/api/cascade_api.py:4546:         resource_path='/api/v1/cascade',
pastel_gateway_sdk/api/cascade_api.py:851:          resource_path='/api/v1/cascade/gateway_requests',
pastel_gateway_sdk/api/cascade_api.py:3208:         resource_path='/api/v1/cascade/gateway_requests/{gateway_request_id}',
pastel_gateway_sdk/api/cascade_api.py:1145:         resource_path='/api/v1/cascade/gateway_results',
pastel_gateway_sdk/api/cascade_api.py:3466:         resource_path='/api/v1/cascade/gateway_results/{gateway_result_id}',

pastel_gateway_sdk/api/cascade_api.py:1403:         resource_path='/api/v1/cascade/originally_submitted_file/{gateway_result_id}',

pastel_gateway_sdk/api/cascade_api.py:296:          resource_path='/api/v1/cascade/all_files_from_request/{gateway_request_id}',
pastel_gateway_sdk/api/cascade_api.py:3724:         resource_path='/api/v1/cascade/stored_file/{gateway_result_id}',
pastel_gateway_sdk/api/cascade_api.py:4240:         resource_path='/api/v1/cascade/stored_file_from_registration_ticket/{registration_ticket_txid}',
pastel_gateway_sdk/api/cascade_api.py:3982:         resource_path='/api/v1/cascade/stored_file_from_activation_ticket/{activation_ticket_txid}',
pastel_gateway_sdk/api/cascade_api.py:2947:         resource_path='/api/v1/cascade/public_stored_file_from_registration_ticket/{registration_ticket_txid}',

pastel_gateway_sdk/api/cascade_api.py:554:          resource_path='/api/v1/cascade/pastel_registration_tickets/{gateway_request_id}',
pastel_gateway_sdk/api/cascade_api.py:2176:         resource_path='/api/v1/cascade/pastel_registration_ticket/{gateway_result_id}',
pastel_gateway_sdk/api/cascade_api.py:2433:         resource_path='/api/v1/cascade/pastel_registration_ticket_from_txid/{registration_ticket_txid}',

pastel_gateway_sdk/api/cascade_api.py:1661:         resource_path='/api/v1/cascade/pastel_activation_ticket/{gateway_result_id}',
pastel_gateway_sdk/api/cascade_api.py:1918:         resource_path='/api/v1/cascade/pastel_activation_ticket_from_txid/{activation_ticket_txid}',

~~pastel_gateway_sdk/api/cascade_api.py:2690:         resource_path='/api/v1/cascade/pastel_ticket_by_stored_file_hash/{stored_file_sha256_hash_as_hex}',~~
pastel_gateway_sdk/api/cascade_api.py:2690:         resource_path='/api/v1/cascade/pastel_registration_ticket_from_stored_file_hash/{stored_file_sha256_hash_as_hex}',

pastel_gateway_sdk/api/cascade_api.py:4823:         resource_path='/api/v1/cascade/result/transfer_pastel_ticket',

### Sense
pastel_gateway_sdk/api/sense_api.py:5842:           resource_path='/api/v1/sense',
pastel_gateway_sdk/api/sense_api.py:1106:           resource_path='/api/v1/sense/gateway_requests',
pastel_gateway_sdk/api/sense_api.py:5261:           resource_path='/api/v1/sense/gateway_requests/{gateway_request_id}',
pastel_gateway_sdk/api/sense_api.py:1400:           resource_path='/api/v1/sense/gateway_results',
pastel_gateway_sdk/api/sense_api.py:5519:           resource_path='/api/v1/sense/gateway_results/{gateway_result_id}',

pastel_gateway_sdk/api/sense_api.py:812:            resource_path='/api/v1/sense/all_raw_output_files_from_request/{gateway_request_id}',
pastel_gateway_sdk/api/sense_api.py:296:            resource_path='/api/v1/sense/all_parsed_output_files_from_request/{gateway_request_id}',

pastel_gateway_sdk/api/sense_api.py:5003:           resource_path='/api/v1/sense/raw_output_file/{gateway_result_id}',
pastel_gateway_sdk/api/sense_api.py:2687:           resource_path='/api/v1/sense/parsed_output_file/{gateway_result_id}',

~~pastel_gateway_sdk/api/sense_api.py:4745:           resource_path='/api/v1/sense/raw_output_file_by_registration_ticket/{registration_ticket_txid}',~~
pastel_gateway_sdk/api/sense_api.py:4745:           resource_path='/api/v1/sense/raw_output_file_from_registration_ticket/{registration_ticket_txid}',
~~pastel_gateway_sdk/api/sense_api.py:2429:           resource_path='/api/v1/sense/parsed_output_file_by_registration_ticket/{registration_ticket_txid}',~~
pastel_gateway_sdk/api/sense_api.py:2429:           resource_path='/api/v1/sense/parsed_output_file_from_registration_ticket/{registration_ticket_txid}',

~~pastel_gateway_sdk/api/sense_api.py:4231:           resource_path='/api/v1/sense/raw_output_file_by_activation_ticket/{activation_ticket_txid}',~~
pastel_gateway_sdk/api/sense_api.py:4231:           resource_path='/api/v1/sense/raw_output_file_from_activation_ticket/{activation_ticket_txid}',
~~pastel_gateway_sdk/api/sense_api.py:1915:           resource_path='/api/v1/sense/parsed_output_file_by_activation_txid/{activation_ticket_txid}',~~
pastel_gateway_sdk/api/sense_api.py:1915:           resource_path='/api/v1/sense/parsed_output_file_from_activation_ticket/{activation_ticket_txid}',

~~pastel_gateway_sdk/api/sense_api.py:4488:           resource_path='/api/v1/sense/raw_output_file_by_pastel_id/{pastel_id_of_user}',~~
pastel_gateway_sdk/api/sense_api.py:4488:           resource_path='/api/v1/sense/raw_output_file_from_pastel_id/{pastel_id_of_user}',
~~pastel_gateway_sdk/api/sense_api.py:2172:           resource_path='/api/v1/sense/parsed_output_file_by_pastel_id/{pastel_id_of_user}',~~
pastel_gateway_sdk/api/sense_api.py:2172:           resource_path='/api/v1/sense/parsed_output_file_from_pastel_id/{pastel_id_of_user}',

pastel_gateway_sdk/api/sense_api.py:1658:           resource_path='/api/v1/sense/originally_submitted_file/{gateway_result_id}',

pastel_gateway_sdk/api/sense_api.py:554:            resource_path='/api/v1/sense/pastel_registration_tickets/{gateway_request_id}',
pastel_gateway_sdk/api/sense_api.py:3717:           resource_path='/api/v1/sense/pastel_registration_ticket/{gateway_result_id}',
pastel_gateway_sdk/api/sense_api.py:3459:           resource_path='/api/v1/sense/pastel_registration_ticket_from_txid/{registration_ticket_txid}',

pastel_gateway_sdk/api/sense_api.py:3202:           resource_path='/api/v1/sense/pastel_activation_ticket/{gateway_result_id}',
pastel_gateway_sdk/api/sense_api.py:2944:           resource_path='/api/v1/sense/pastel_activation_ticket_from_txid/{activation_ticket_txid}',

~~pastel_gateway_sdk/api/sense_api.py:3974:           resource_path='/api/v1/sense/pastel_ticket_by_media_file_hash/{media_file_sha256_hash}',~~
pastel_gateway_sdk/api/sense_api.py:3974:           resource_path='/api/v1/sense/pastel_registration_ticket_from_media_file_hash/{media_file_sha256_hash}',

pastel_gateway_sdk/api/sense_api.py:6119:           resource_path='/api/v1/sense/result/transfer_pastel_ticket',

### NFT
pastel_gateway_sdk/api/nft_api.py:7163:             resource_path='/api/v1/nft',
pastel_gateway_sdk/api/nft_api.py:7434:             resource_path='/api/v1/nft/step_1_upload_image_file',
pastel_gateway_sdk/api/nft_api.py:7790:             resource_path='/api/v1/nft/step_2_process_nft',

pastel_gateway_sdk/api/nft_api.py:1365:             resource_path='/api/v1/nft/gateway_requests',
pastel_gateway_sdk/api/nft_api.py:5777:             resource_path='/api/v1/nft/gateway_requests/{gateway_request_id}',
pastel_gateway_sdk/api/nft_api.py:1659:             resource_path='/api/v1/nft/gateway_results',
pastel_gateway_sdk/api/nft_api.py:6035:             resource_path='/api/v1/nft/gateway_results/{gateway_result_id}',

pastel_gateway_sdk/api/nft_api.py:1917:             resource_path='/api/v1/nft/originally_submitted_file/{gateway_result_id}',
pastel_gateway_sdk/api/nft_api.py:6809:             resource_path='/api/v1/nft/stored_file/{gateway_result_id}',
pastel_gateway_sdk/api/nft_api.py:6551:             resource_path='/api/v1/nft/stored_file_from_registration_ticket/{registration_ticket_txid}',
pastel_gateway_sdk/api/nft_api.py:6293:             resource_path='/api/v1/nft/stored_file_from_activation_ticket/{activation_ticket_txid}',
pastel_gateway_sdk/api/nft_api.py:4490:             resource_path='/api/v1/nft/public_stored_file_from_registration_ticket/{registration_ticket_txid}',

pastel_gateway_sdk/api/nft_api.py:297:              resource_path='/api/v1/nft/all_files_from_request/{gateway_request_id}',

pastel_gateway_sdk/api/nft_api.py:555:              resource_path='/api/v1/nft/all_parsed_dd_result_files_from_request/{gateway_request_id}',
pastel_gateway_sdk/api/nft_api.py:1071:             resource_path='/api/v1/nft/all_raw_dd_result_files_from_request/{gateway_request_id}',

pastel_gateway_sdk/api/nft_api.py:2946:             resource_path='/api/v1/nft/parsed_dd_result_file/{gateway_result_id}',
~~pastel_gateway_sdk/api/nft_api.py:2688:             resource_path='/api/v1/nft/parsed_dd_result_file_by_registration_ticket/{registration_ticket_txid}',~~
pastel_gateway_sdk/api/nft_api.py:2688:             resource_path='/api/v1/nft/parsed_dd_result_file_from_registration_ticket/{registration_ticket_txid}',
~~pastel_gateway_sdk/api/nft_api.py:2174:             resource_path='/api/v1/nft/parsed_dd_result_file_by_activation_txid/{activation_ticket_txid}',~~
pastel_gateway_sdk/api/nft_api.py:2174:             resource_path='/api/v1/nft/parsed_dd_result_file_from_activation_ticket/{activation_ticket_txid}',
~~pastel_gateway_sdk/api/nft_api.py:2431:             resource_path='/api/v1/nft/parsed_dd_result_file_by_pastel_id/{pastel_id_of_user}',~~
pastel_gateway_sdk/api/nft_api.py:2431:             resource_path='/api/v1/nft/parsed_dd_result_file_from_pastel_id/{pastel_id_of_user}',

pastel_gateway_sdk/api/nft_api.py:5519:             resource_path='/api/v1/nft/raw_dd_result_file/{gateway_result_id}',
~~pastel_gateway_sdk/api/nft_api.py:5261:             resource_path='/api/v1/nft/raw_dd_result_file_by_registration_ticket/{registration_ticket_txid}',~~
pastel_gateway_sdk/api/nft_api.py:5261:             resource_path='/api/v1/nft/raw_dd_result_file_from_registration_ticket/{registration_ticket_txid}',
~~pastel_gateway_sdk/api/nft_api.py:4747:             resource_path='/api/v1/nft/raw_dd_result_file_by_activation_ticket/{activation_ticket_txid}',~~
pastel_gateway_sdk/api/nft_api.py:4747:             resource_path='/api/v1/nft/raw_dd_result_file_from_activation_ticket/{activation_ticket_txid}',
~~pastel_gateway_sdk/api/nft_api.py:5004:             resource_path='/api/v1/nft/raw_dd_result_file_by_pastel_id/{pastel_id_of_user}',~~
pastel_gateway_sdk/api/nft_api.py:5004:             resource_path='/api/v1/nft/raw_dd_result_file_from_pastel_id/{pastel_id_of_user}',

pastel_gateway_sdk/api/nft_api.py:813:              resource_path='/api/v1/nft/pastel_registration_tickets/{gateway_request_id}',
pastel_gateway_sdk/api/nft_api.py:3976:             resource_path='/api/v1/nft/pastel_registration_ticket/{gateway_result_id}',
pastel_gateway_sdk/api/nft_api.py:3718:             resource_path='/api/v1/nft/pastel_registration_ticket_from_txid/{registration_ticket_txid}',

pastel_gateway_sdk/api/nft_api.py:3461:             resource_path='/api/v1/nft/pastel_activation_ticket/{gateway_result_id}',
pastel_gateway_sdk/api/nft_api.py:3203:             resource_path='/api/v1/nft/pastel_activation_ticket_from_txid/{activation_ticket_txid}',

~~pastel_gateway_sdk/api/nft_api.py:4233:             resource_path='/api/v1/nft/pastel_ticket_by_media_file_hash/{media_file_sha256_hash}',~~
pastel_gateway_sdk/api/nft_api.py:4233:             resource_path='/api/v1/nft/pastel_registration_ticket_from_media_file_hash/{media_file_sha256_hash}',

pastel_gateway_sdk/api/nft_api.py:8067:             resource_path='/api/v1/nft/result/transfer_pastel_ticket',

### Collection
pastel_gateway_sdk/api/collection_api.py:433:       resource_path='/api/v1/collection/nft',
pastel_gateway_sdk/api/collection_api.py:1070:      resource_path='/api/v1/collection/nft/collections',
pastel_gateway_sdk/api/collection_api.py:1568:      resource_path='/api/v1/collection/nft/collections/{collection_id}',

pastel_gateway_sdk/api/collection_api.py:830:       resource_path='/api/v1/collection/sense',
pastel_gateway_sdk/api/collection_api.py:1310:      resource_path='/api/v1/collection/sense/collections',
pastel_gateway_sdk/api/collection_api.py:1826:      resource_path='/api/v1/collection/sense/collections/{collection_id}',
