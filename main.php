<?php
// File: src/Controller/PagesController.php
namespace App\Controller;

use Cake\Http\Response;
use Cake\Http\ServerRequest;

class PagesController extends \Cake\Controller\Controller
{
    // Single action to load index.html
    public function index()
    {
        // Path to index.html in webroot
        $path = WWW_ROOT . 'index.html';

        if (!file_exists($path)) {
            // If file does not exist, return 404
            throw new \Cake\Http\Exception\NotFoundException('File not found');
        }

        // Load content of index.html
        $content = file_get_contents($path);

        // Return HTML response directly
        $this->response = $this->response
                               ->withType('html')
                               ->withStringBody($content);
        return $this->response;
    }
}

// =====================
// Route (put this in config/routes.php)
// =====================
$routes->connect('/', ['controller' => 'Pages', 'action' => 'index']);
